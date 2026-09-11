#!/usr/bin/env python3
"""Calculate responsive expanded phone Live View card geometry exactly."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def decimal_value(value: Fraction) -> float:
    return float(value)


def rounded_pixel(value: Fraction) -> int:
    """Round a non-negative exact fraction to the nearest integer, half up."""
    if value < 0:
        raise ValueError("Pixel coordinates must be non-negative.")
    return (2 * value.numerator + value.denominator) // (2 * value.denominator)


def frame(exact: tuple[Fraction, Fraction, Fraction, Fraction]) -> dict[str, object]:
    labels = ("x", "y", "width", "height")
    return {
        "exact_vp": {key: fraction_text(value) for key, value in zip(labels, exact)},
        "decimal_vp": {key: decimal_value(value) for key, value in zip(labels, exact)},
    }


def calculate(width_vp: Fraction, height_vp: Fraction) -> dict[str, object]:
    if width_vp <= 32:
        raise ValueError("Canvas width must exceed the two 16 vp side margins.")
    if height_vp <= 50:
        raise ValueError("Canvas height must exceed the 50 vp top coordinate.")

    card_width = width_vp - 32
    card_height = card_width * 6 / 17
    card = (Fraction(16), Fraction(50), card_width, card_height)
    fixed = (Fraction(12), Fraction(10), card_width - 80, Fraction(52))
    auxiliary = (card_width - 56, Fraction(14), Fraction(44), Fraction(44))
    extension = (Fraction(12), Fraction(72), card_width - 24, card_height - 84)

    if fixed[2] <= 0 or extension[2] <= 0 or extension[3] < 0:
        raise ValueError(
            "The calculated card cannot contain the required regions; use an explicit "
            "device-specific override rather than clipping or distorting content."
        )
    if card[1] + card[3] > height_vp:
        raise ValueError("The calculated card extends below the logical canvas.")

    return {
        "logical_canvas_vp": {
            "width_exact": fraction_text(width_vp),
            "height_exact": fraction_text(height_vp),
        },
        "formula": {
            "card_width": "W - 32",
            "card_height": "(W - 32) * 6 / 17",
            "card_frame": "(16, 50, W - 32, (W - 32) * 6 / 17)",
        },
        "card": frame(card),
        "corner_radius_vp": 20,
        "regions": {
            "fixed": frame(fixed),
            "auxiliary_optional": frame(auxiliary),
            "extension": frame(extension),
        },
        "material": {
            "underlay_blurred": True,
            "neutral_dark_overlay_opacity": 0.48,
            "neutral_outline_opacity": 0.25,
            "backdrop_blur_design_value_when_required": 50,
        },
    }


def add_raster(
    result: dict[str, object],
    width_vp: Fraction,
    height_vp: Fraction,
    width_px: int,
    height_px: int,
) -> None:
    scale_x = Fraction(width_px, 1) / width_vp
    scale_y = Fraction(height_px, 1) / height_vp

    def rasterize(vp_frame: dict[str, object]) -> dict[str, object]:
        exact = vp_frame["exact_vp"]
        x = Fraction(exact["x"])
        y = Fraction(exact["y"])
        width = Fraction(exact["width"])
        height = Fraction(exact["height"])
        values = (x * scale_x, y * scale_y, width * scale_x, height * scale_y)
        right = (x + width) * scale_x
        bottom = (y + height) * scale_y
        return {
            "exact_px": {
                key: fraction_text(value)
                for key, value in zip(("x", "y", "width", "height"), values)
            },
            "rounded_px": {
                key: rounded_pixel(value)
                for key, value in zip(("x", "y", "width", "height"), values)
            },
            "rounded_edges_px": {
                "left": rounded_pixel(values[0]),
                "top": rounded_pixel(values[1]),
                "right": rounded_pixel(right),
                "bottom": rounded_pixel(bottom),
            },
        }

    result["raster_canvas_px"] = {"width": width_px, "height": height_px}
    result["raster_scale_exact"] = {
        "x_px_per_vp": fraction_text(scale_x),
        "y_px_per_vp": fraction_text(scale_y),
    }
    result["card_raster"] = rasterize(result["card"])
    result["regions_raster"] = {
        name: rasterize(region) for name, region in result["regions"].items()
    }
    result["corner_radius_raster_px"] = {
        "x_axis": rounded_pixel(Fraction(20) * scale_x),
        "y_axis": rounded_pixel(Fraction(20) * scale_y),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate responsive expanded phone Live View card geometry."
    )
    parser.add_argument("--width-vp", required=True)
    parser.add_argument("--height-vp", required=True)
    parser.add_argument("--width-px", type=int)
    parser.add_argument("--height-px", type=int)
    args = parser.parse_args()

    if (args.width_px is None) != (args.height_px is None):
        parser.error("Provide --width-px and --height-px together, or omit both.")
    if args.width_px is not None and (args.width_px <= 0 or args.height_px <= 0):
        parser.error("Raster dimensions must be positive.")

    try:
        width_vp = Fraction(args.width_vp)
        height_vp = Fraction(args.height_vp)
        result = calculate(width_vp, height_vp)
        if args.width_px is not None:
            add_raster(result, width_vp, height_vp, args.width_px, args.height_px)
    except (ValueError, ZeroDivisionError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
