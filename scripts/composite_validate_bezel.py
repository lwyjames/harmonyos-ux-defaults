#!/usr/bin/env python3
"""Composite a mapped HarmonyOS bezel and validate every inner edge/corner."""

from __future__ import annotations

import argparse
import gc
import json
import math
import sys
from pathlib import Path
from typing import Iterable

try:
    import numpy as np
    from PIL import Image, ImageChops, ImageDraw
    from scipy import ndimage
except ImportError as exc:  # pragma: no cover - environment-specific failure
    raise SystemExit(
        "This helper requires Pillow, NumPy, and SciPy. "
        "Install them with: python -m pip install pillow numpy scipy"
    ) from exc


Image.MAX_IMAGE_PIXELS = None

SKILL_ROOT = Path(__file__).resolve().parent.parent
DEVICE_MAP = {
    "pura-x-max-unfolded-portrait": {
        "screen_size": (1828, 2584),
        "bezel": SKILL_ROOT
        / "assets/device-bezels/pura-x-max-unfolded-portrait.png",
    },
    "pura-x-max-unfolded-landscape": {
        "screen_size": (2584, 1828),
        "bezel": SKILL_ROOT
        / "assets/device-bezels/pura-x-max-unfolded-portrait.png",
        "bezel_rotation": "clockwise_90",
    },
    "pura-x-view-front": {
        "screen_size": (1320, 2232),
        "bezel": SKILL_ROOT / "assets/device-bezels/pura-x-view-front.png",
    },
    "pura-90-pro-max-portrait": {
        "screen_size": (1308, 2880),
        "bezel": SKILL_ROOT
        / "assets/device-bezels/pura-90-pro-max-portrait.png",
    },
}

REGION_NAMES = (
    "upper_edge",
    "bottom_edge",
    "left_edge",
    "right_edge",
    "upper_left_corner",
    "upper_right_corner",
    "bottom_left_corner",
    "bottom_right_corner",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Composite a fully opaque HarmonyOS screen beneath its mapped official "
            "bezel, derive four-direction overscan from alpha, and validate seams."
        )
    )
    parser.add_argument("--device", required=True, choices=sorted(DEVICE_MAP))
    parser.add_argument("--screen", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument(
        "--diagnostics-dir",
        type=Path,
        help=(
            "Optional directory for native-pixel inspection sheets on white, black, "
            "and saturated magenta backgrounds. Inspect them at 400%% zoom."
        ),
    )
    return parser.parse_args()


def count_nonzero(image: Image.Image) -> int:
    histogram = image.histogram()
    return int(sum(histogram[1:]))


def binary_regions(alpha: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return center-connected inner aperture and border-connected exterior."""
    transparent = alpha < 255
    eight_connected = np.ones((3, 3), dtype=bool)

    exterior_seed = np.zeros_like(transparent)
    exterior_seed[0, :] = transparent[0, :]
    exterior_seed[-1, :] = transparent[-1, :]
    exterior_seed[:, 0] = transparent[:, 0]
    exterior_seed[:, -1] = transparent[:, -1]
    exterior = ndimage.binary_propagation(
        exterior_seed, structure=eight_connected, mask=transparent
    )

    height, width = transparent.shape
    center_y, center_x = height // 2, width // 2
    if not transparent[center_y, center_x] or exterior[center_y, center_x]:
        raise ValueError(
            "The bezel center is not an isolated transparent screen opening. "
            "The official asset needs an explicit interior seed or corrected alpha."
        )

    aperture_seed = np.zeros_like(transparent)
    aperture_seed[center_y, center_x] = True
    aperture = ndimage.binary_propagation(
        aperture_seed, structure=eight_connected, mask=transparent
    )
    if not aperture.any() or np.any(aperture & exterior):
        raise ValueError("Could not isolate the inner aperture from exterior transparency.")
    return aperture, exterior


def aperture_geometry(aperture: np.ndarray) -> dict[str, object]:
    ys = np.flatnonzero(aperture.any(axis=1))
    xs = np.flatnonzero(aperture.any(axis=0))
    if not len(xs) or not len(ys):
        raise ValueError("The center-connected aperture is empty.")

    left, top = int(xs[0]), int(ys[0])
    right, bottom = int(xs[-1] + 1), int(ys[-1] + 1)
    sub = aperture[top:bottom, left:right]
    height, width = sub.shape

    first_y = np.argmax(sub, axis=0)
    last_y = height - 1 - np.argmax(sub[::-1, :], axis=0)
    first_x = np.argmax(sub, axis=1)
    last_x = width - 1 - np.argmax(sub[:, ::-1], axis=1)

    def first_true(values: np.ndarray) -> int:
        matches = np.flatnonzero(values)
        return int(matches[0] + 1) if len(matches) else max(1, min(width, height) // 20)

    corners = {
        "upper_left": {
            "width": first_true(first_y <= 1),
            "height": first_true(first_x <= 1),
        },
        "upper_right": {
            "width": first_true((first_y <= 1)[::-1]),
            "height": first_true(last_x >= width - 2),
        },
        "bottom_left": {
            "width": first_true(last_y >= height - 2),
            "height": first_true((first_x <= 1)[::-1]),
        },
        "bottom_right": {
            "width": first_true((last_y >= height - 2)[::-1]),
            "height": first_true((last_x >= width - 2)[::-1]),
        },
    }

    return {
        "bbox": (left, top, right, bottom),
        "first_y": first_y,
        "last_y": last_y,
        "first_x": first_x,
        "last_x": last_x,
        "corners": corners,
    }


def mode(values: np.ndarray) -> int:
    return int(np.bincount(values.astype(np.int64)).argmax())


def partial_run(values: Iterable[int]) -> int:
    run = 0
    for value in values:
        value = int(value)
        if value == 0:
            break
        if value == 255:
            break
        run += 1
    return run


def alpha_transition_widths(
    alpha: np.ndarray, geometry: dict[str, object]
) -> dict[str, int]:
    left, top, right, bottom = geometry["bbox"]  # type: ignore[misc]
    first_y = geometry["first_y"]  # type: ignore[assignment]
    last_y = geometry["last_y"]  # type: ignore[assignment]
    first_x = geometry["first_x"]  # type: ignore[assignment]
    last_x = geometry["last_x"]  # type: ignore[assignment]
    width, height = right - left, bottom - top

    x0, x1 = max(0, width // 5), min(width, math.ceil(width * 4 / 5))
    y0, y1 = max(0, height // 5), min(height, math.ceil(height * 4 / 5))
    center_x = np.arange(x0, x1, dtype=np.int64)
    center_y = np.arange(y0, y1, dtype=np.int64)

    top_level = mode(first_y[center_x])
    bottom_level = mode(last_y[center_x])
    left_level = mode(first_x[center_y])
    right_level = mode(last_x[center_y])

    top_samples = center_x[np.abs(first_y[center_x] - top_level) <= 1]
    bottom_samples = center_x[np.abs(last_y[center_x] - bottom_level) <= 1]
    left_samples = center_y[np.abs(first_x[center_y] - left_level) <= 1]
    right_samples = center_y[np.abs(last_x[center_y] - right_level) <= 1]

    upper = max(
        (
            partial_run(alpha[top + int(first_y[x]) : bottom, left + int(x)])
            for x in top_samples
        ),
        default=0,
    )
    lower = max(
        (
            partial_run(
                alpha[top : top + int(last_y[x]) + 1, left + int(x)][::-1]
            )
            for x in bottom_samples
        ),
        default=0,
    )
    left_width = max(
        (
            partial_run(alpha[top + int(y), left + int(first_x[y]) : right])
            for y in left_samples
        ),
        default=0,
    )
    right_width = max(
        (
            partial_run(
                alpha[top + int(y), left : left + int(last_x[y]) + 1][::-1]
            )
            for y in right_samples
        ),
        default=0,
    )
    return {
        "upper": int(upper),
        "bottom": int(lower),
        "left": int(left_width),
        "right": int(right_width),
    }


def overscan_from_alpha(alpha_widths: dict[str, int]) -> tuple[dict[str, int], dict[str, int]]:
    safety = {
        side: max(1, math.ceil((width + 1) / 2))
        for side, width in alpha_widths.items()
    }
    overscan = {
        side: alpha_widths[side] + safety[side]
        for side in ("upper", "bottom", "left", "right")
    }
    return overscan, safety


def extrude(
    image: Image.Image, *, left: int, right: int, upper: int, bottom: int
) -> Image.Image:
    """Extend edge and corner pixels without altering the original image area."""
    width, height = image.size
    out = Image.new("RGBA", (width + left + right, height + upper + bottom))
    out.paste(image, (left, upper))

    if upper:
        row = image.crop((0, 0, width, 1)).resize((width, upper), Image.Resampling.NEAREST)
        out.paste(row, (left, 0))
    if bottom:
        row = image.crop((0, height - 1, width, height)).resize(
            (width, bottom), Image.Resampling.NEAREST
        )
        out.paste(row, (left, upper + height))
    if left:
        column = image.crop((0, 0, 1, height)).resize(
            (left, height), Image.Resampling.NEAREST
        )
        out.paste(column, (0, upper))
    if right:
        column = image.crop((width - 1, 0, width, height)).resize(
            (right, height), Image.Resampling.NEAREST
        )
        out.paste(column, (left + width, upper))

    corners = (
        ((0, 0), (0, 0, left, upper)),
        ((width - 1, 0), (left + width, 0, left + width + right, upper)),
        ((0, height - 1), (0, upper + height, left, upper + height + bottom)),
        (
            (width - 1, height - 1),
            (
                left + width,
                upper + height,
                left + width + right,
                upper + height + bottom,
            ),
        ),
    )
    draw = ImageDraw.Draw(out)
    for source_xy, rectangle in corners:
        if rectangle[0] < rectangle[2] and rectangle[1] < rectangle[3]:
            draw.rectangle(
                (rectangle[0], rectangle[1], rectangle[2] - 1, rectangle[3] - 1),
                fill=image.getpixel(source_xy),
            )
    return out


def map_screen_to_aperture(screen: Image.Image, bbox: tuple[int, int, int, int]) -> Image.Image:
    target_width = bbox[2] - bbox[0]
    target_height = bbox[3] - bbox[1]
    source_width, source_height = screen.size
    source_ratio = source_width / source_height
    target_ratio = target_width / target_height
    relative_error = abs(target_ratio / source_ratio - 1.0)
    if relative_error > 0.002:
        raise ValueError(
            "Official aperture ratio and documented screen ratio differ by more than "
            f"0.2% ({relative_error:.4%}); refusing to stretch or crop the UI."
        )

    scale = min(target_width / source_width, target_height / source_height)
    mapped_width = min(target_width, max(1, round(source_width * scale)))
    mapped_height = min(target_height, max(1, round(source_height * scale)))
    mapped = screen.resize((mapped_width, mapped_height), Image.Resampling.LANCZOS)

    gap_x, gap_y = target_width - mapped_width, target_height - mapped_height
    gap_left, gap_upper = gap_x // 2, gap_y // 2
    return extrude(
        mapped,
        left=gap_left,
        right=gap_x - gap_left,
        upper=gap_upper,
        bottom=gap_y - gap_upper,
    )


def classify_uncovered(
    uncovered: Image.Image,
    bbox: tuple[int, int, int, int],
    corners: dict[str, dict[str, int]],
) -> dict[str, int]:
    counts = {name: 0 for name in REGION_NAMES}
    if not count_nonzero(uncovered):
        return counts

    pixels = np.asarray(uncovered)
    ys, xs = np.nonzero(pixels)
    left, top, right, bottom = bbox
    width, height = right - left, bottom - top

    for x, y in zip(xs.tolist(), ys.tolist()):
        xr, yr = x - left, y - top
        if xr < corners["upper_left"]["width"] and yr < corners["upper_left"]["height"]:
            region = "upper_left_corner"
        elif xr >= width - corners["upper_right"]["width"] and yr < corners["upper_right"]["height"]:
            region = "upper_right_corner"
        elif xr < corners["bottom_left"]["width"] and yr >= height - corners["bottom_left"]["height"]:
            region = "bottom_left_corner"
        elif xr >= width - corners["bottom_right"]["width"] and yr >= height - corners["bottom_right"]["height"]:
            region = "bottom_right_corner"
        else:
            distances = {
                "upper_edge": max(0, yr),
                "bottom_edge": max(0, height - 1 - yr),
                "left_edge": max(0, xr),
                "right_edge": max(0, width - 1 - xr),
            }
            region = min(distances, key=distances.get)
        counts[region] += 1
    return counts


def flatten(image: Image.Image, background: tuple[int, int, int]) -> Image.Image:
    base = Image.new("RGBA", image.size, background + (255,))
    base.alpha_composite(image)
    return base.convert("RGB")


def make_inspection_sheet(
    composite: Image.Image,
    bbox: tuple[int, int, int, int],
    corners: dict[str, dict[str, int]],
    overscan: dict[str, int],
    background: tuple[int, int, int],
    output: Path,
) -> None:
    """Preserve native pixels in a compact sheet covering four full edges/corners."""
    left, top, right, bottom = bbox
    canvas_width, canvas_height = composite.size
    edge_depth = max(48, 8 * max(overscan.values()))

    boxes = {
        "upper edge": (
            left,
            max(0, top - edge_depth),
            right,
            min(canvas_height, top + edge_depth),
        ),
        "bottom edge": (
            left,
            max(0, bottom - edge_depth),
            right,
            min(canvas_height, bottom + edge_depth),
        ),
        "left edge": (
            max(0, left - edge_depth),
            top,
            min(canvas_width, left + edge_depth),
            bottom,
        ),
        "right edge": (
            max(0, right - edge_depth),
            top,
            min(canvas_width, right + edge_depth),
            bottom,
        ),
    }

    edge_rows: list[tuple[str, Image.Image]] = []
    for label, box in boxes.items():
        crop = flatten(composite.crop(box), background)
        if label in {"left edge", "right edge"}:
            crop = crop.transpose(Image.Transpose.ROTATE_90)
        edge_rows.append((label, crop))

    corner_span = max(
        edge_depth,
        *(value for corner in corners.values() for value in corner.values()),
    )
    corner_boxes = {
        "upper-left": (
            max(0, left - corner_span),
            max(0, top - corner_span),
            min(canvas_width, left + corner_span),
            min(canvas_height, top + corner_span),
        ),
        "upper-right": (
            max(0, right - corner_span),
            max(0, top - corner_span),
            min(canvas_width, right + corner_span),
            min(canvas_height, top + corner_span),
        ),
        "bottom-left": (
            max(0, left - corner_span),
            max(0, bottom - corner_span),
            min(canvas_width, left + corner_span),
            min(canvas_height, bottom + corner_span),
        ),
        "bottom-right": (
            max(0, right - corner_span),
            max(0, bottom - corner_span),
            min(canvas_width, right + corner_span),
            min(canvas_height, bottom + corner_span),
        ),
    }
    corner_images = [
        (label, flatten(composite.crop(box), background))
        for label, box in corner_boxes.items()
    ]

    label_height = 24
    row_width = max(image.width for _, image in edge_rows)
    corner_width = sum(image.width for _, image in corner_images)
    sheet_width = max(row_width, corner_width)
    sheet_height = sum(label_height + image.height for _, image in edge_rows)
    sheet_height += label_height + max(image.height for _, image in corner_images)
    sheet = Image.new("RGB", (sheet_width, sheet_height), background)
    draw = ImageDraw.Draw(sheet)

    y = 0
    text_color = (255, 255, 255) if sum(background) < 240 else (0, 0, 0)
    for label, image in edge_rows:
        draw.text((4, y + 4), f"{label} — native pixels; inspect at 400%", fill=text_color)
        y += label_height
        sheet.paste(image, (0, y))
        y += image.height

    draw.text((4, y + 4), "all four corners and edge/curve transitions", fill=text_color)
    y += label_height
    x = 0
    for label, image in corner_images:
        sheet.paste(image, (x, y))
        draw.text((x + 4, y + 4), label, fill=text_color)
        x += image.width

    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, format="PNG", optimize=True)


def main() -> int:
    args = parse_args()
    mapping = DEVICE_MAP[args.device]
    expected_size = mapping["screen_size"]
    bezel_path = mapping["bezel"]

    with Image.open(args.screen) as source:
        screen = source.convert("RGBA")
    if screen.size != expected_size:
        raise ValueError(
            f"{args.device} requires a {expected_size[0]} x {expected_size[1]} px "
            f"screen; received {screen.width} x {screen.height} px."
        )
    source_alpha = screen.getchannel("A")
    source_uncovered = screen.width * screen.height - source_alpha.histogram()[255]
    if source_uncovered:
        raise ValueError(
            f"The source screen is not fully opaque ({source_uncovered} non-opaque pixels)."
        )
    del source_alpha

    with Image.open(bezel_path) as source:
        bezel = source.convert("RGBA")
    bezel_rotation = mapping.get("bezel_rotation", "none")
    if bezel_rotation == "clockwise_90":
        bezel = bezel.transpose(Image.Transpose.ROTATE_270)
    elif bezel_rotation != "none":
        raise ValueError(f"Unsupported mapped bezel rotation: {bezel_rotation}")
    bezel_alpha = bezel.getchannel("A")
    alpha_array = np.asarray(bezel_alpha)
    aperture, exterior = binary_regions(alpha_array)
    geometry = aperture_geometry(aperture)
    bbox = geometry["bbox"]  # type: ignore[assignment]
    alpha_widths = alpha_transition_widths(alpha_array, geometry)
    overscan, safety = overscan_from_alpha(alpha_widths)

    aperture_pixels = int(np.count_nonzero(aperture))
    exterior_pixels = int(np.count_nonzero(exterior))
    aperture_mask = Image.fromarray((aperture.astype(np.uint8) * 255), mode="L")
    exterior_mask = Image.fromarray((exterior.astype(np.uint8) * 255), mode="L")
    del alpha_array, aperture, exterior
    gc.collect()

    mapped_screen = map_screen_to_aperture(screen, bbox)
    extended_screen = extrude(
        mapped_screen,
        left=overscan["left"],
        right=overscan["right"],
        upper=overscan["upper"],
        bottom=overscan["bottom"],
    )
    origin = (bbox[0] - overscan["left"], bbox[1] - overscan["upper"])
    if (
        origin[0] < 0
        or origin[1] < 0
        or origin[0] + extended_screen.width > bezel.width
        or origin[1] + extended_screen.height > bezel.height
    ):
        raise ValueError("Calculated overscan exceeds the official bezel canvas.")

    screen_canvas = Image.new("RGBA", bezel.size)
    screen_canvas.paste(extended_screen, origin)
    screen_canvas_alpha = screen_canvas.getchannel("A")
    screen_canvas_alpha.paste(0, (0, 0), exterior_mask)
    screen_canvas.putalpha(screen_canvas_alpha)

    uncovered = ImageChops.multiply(aperture_mask, ImageChops.invert(screen_canvas_alpha))
    global_uncovered = count_nonzero(uncovered)
    regional_uncovered = classify_uncovered(
        uncovered, bbox, geometry["corners"]  # type: ignore[arg-type]
    )
    exterior_screen_leak = count_nonzero(
        ImageChops.multiply(screen_canvas_alpha, exterior_mask)
    )

    screen_canvas.alpha_composite(bezel)
    final_alpha = screen_canvas.getchannel("A")
    exterior_alpha_mismatch = count_nonzero(
        ImageChops.multiply(
            ImageChops.difference(final_alpha, bezel_alpha), exterior_mask
        )
    )
    opaque_mask = bezel_alpha.point(lambda value: 255 if value == 255 else 0)
    channel_difference = Image.new("L", bezel.size)
    for channel in ImageChops.difference(screen_canvas, bezel).split():
        channel_difference = ImageChops.lighter(channel_difference, channel)
    opaque_bezel_mismatch = count_nonzero(
        ImageChops.multiply(channel_difference, opaque_mask)
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    screen_canvas.save(args.output, format="PNG", optimize=True)

    diagnostic_files: list[str] = []
    if args.diagnostics_dir:
        backgrounds = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "saturated-magenta": (255, 0, 255),
        }
        for name, color in backgrounds.items():
            path = args.diagnostics_dir / f"inspection-{name}.png"
            make_inspection_sheet(
                screen_canvas,
                bbox,
                geometry["corners"],  # type: ignore[arg-type]
                overscan,
                color,
                path,
            )
            diagnostic_files.append(str(path))

    passed = (
        global_uncovered == 0
        and all(value == 0 for value in regional_uncovered.values())
        and exterior_screen_leak == 0
        and exterior_alpha_mismatch == 0
        and opaque_bezel_mismatch == 0
        and screen_canvas.size == bezel.size
    )
    report = {
        "status": "PASS" if passed else "FAIL",
        "device": args.device,
        "screen": {
            "path": str(args.screen),
            "documented_size": list(expected_size),
            "fully_opaque": source_uncovered == 0,
            "non_opaque_source_pixels": int(source_uncovered),
            "visible_coordinate_mapping": "single proportional transform; edge extrusion only outside mapped UI",
        },
        "bezel": {
            "path": str(bezel_path),
            "source_rotation": bezel_rotation,
            "camera_position": (
                "upper-right" if bezel_rotation == "clockwise_90" else "source-defined"
            ),
            "native_size": list(bezel.size),
            "output_size": list(screen_canvas.size),
            "resized_or_cropped": False,
            "opaque_pixel_mismatch_count": opaque_bezel_mismatch,
        },
        "alpha_geometry": {
            "inner_aperture_method": "center-connected alpha<255 component",
            "exterior_method": "border-connected alpha<255 component",
            "aperture_bbox": list(bbox),
            "aperture_pixel_count": aperture_pixels,
            "exterior_pixel_count": exterior_pixels,
            "antialias_transition_width_px": alpha_widths,
            "hidden_safety_margin_px": safety,
            "directional_overscan_px": overscan,
            "corner_transition_geometry_px": geometry["corners"],
        },
        "acceptance_checks": {
            "all_inner_aperture_uncovered_pixels": global_uncovered,
            "regional_uncovered_pixels": regional_uncovered,
            "exterior_screen_leak_pixels": exterior_screen_leak,
            "exterior_alpha_mismatch_pixels": exterior_alpha_mismatch,
        },
        "diagnostic_files": diagnostic_files,
        "acceptance_criterion": (
            "The active screen continuously meets the official bezel's antialiased "
            "inner boundary across the complete upper, bottom, left, and right edges "
            "and all four corners. Every partially or fully transparent inner-aperture "
            "pixel has opaque screen content beneath it, every directional uncovered-"
            "pixel count is zero, and no screen content leaks outside the official "
            "device silhouette."
        ),
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if passed else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
