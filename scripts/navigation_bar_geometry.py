#!/usr/bin/env python3
"""Calculate corrected HarmonyOS navigation-indicator geometry."""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Frame:
    x: float
    y: float
    width: float
    height: float

    def as_dict(self) -> dict[str, float]:
        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
        }


def indicator_width(width_vp: float) -> tuple[float, str]:
    if width_vp < 360:
        raise ValueError(
            "The supplied geometry is defined for logical widths >= 360 vp; "
            "use the native system component/insets for narrower surfaces."
        )
    if width_vp < 600:
        return 112.0, "360 <= W < 600: 112 vp"
    if width_vp <= 840:
        return width_vp / 3.0 - 48.0, "600 <= W <= 840: W / 3 - 48 vp"
    return width_vp / 4.0 - 48.0, "W > 840: W / 4 - 48 vp"


def calculate(width_vp: float, height_vp: float) -> dict[str, object]:
    if not math.isfinite(width_vp) or not math.isfinite(height_vp):
        raise ValueError("Logical dimensions must be finite numbers.")
    if height_vp <= 28:
        raise ValueError("Logical height must exceed the 28 vp interaction region.")

    bar_width, branch = indicator_width(width_vp)
    indicator = Frame(
        x=(width_vp - bar_width) / 2.0,
        y=height_vp - 12.0,
        width=bar_width,
        height=6.0,
    )
    interaction = Frame(
        x=width_vp * 0.325,
        y=height_vp - 28.0,
        width=width_vp * 0.35,
        height=28.0,
    )
    return {
        "logical_screen_vp": {"width": width_vp, "height": height_vp},
        "width_rule": branch,
        "visible_indicator_vp": indicator.as_dict(),
        "visible_indicator_bottom_gap_vp": 6.0,
        "visible_indicator_centerline_gap_vp": 9.0,
        "derived_capsule_radius_vp": 3.0,
        "interaction_region_vp": interaction.as_dict(),
        "interaction_region_visible": False,
    }


def pixel_frame(frame: dict[str, float], scale_x: float, scale_y: float) -> dict[str, object]:
    left = frame["x"] * scale_x
    top = frame["y"] * scale_y
    right = (frame["x"] + frame["width"]) * scale_x
    bottom = (frame["y"] + frame["height"]) * scale_y
    return {
        "float_bounds": {"left": left, "top": top, "right": right, "bottom": bottom},
        "nearest_integer_bounds": {
            "left": math.floor(left + 0.5),
            "top": math.floor(top + 0.5),
            "right": math.floor(right + 0.5),
            "bottom": math.floor(bottom + 0.5),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate the corrected responsive HarmonyOS navigation-bar geometry."
    )
    parser.add_argument("--width-vp", type=float, required=True)
    parser.add_argument("--height-vp", type=float, required=True)
    parser.add_argument("--width-px", type=int)
    parser.add_argument("--height-px", type=int)
    args = parser.parse_args()

    if (args.width_px is None) != (args.height_px is None):
        parser.error("Provide --width-px and --height-px together, or omit both.")
    if args.width_px is not None and (args.width_px <= 0 or args.height_px <= 0):
        parser.error("Pixel dimensions must be positive.")

    try:
        result = calculate(args.width_vp, args.height_vp)
    except ValueError as exc:
        parser.error(str(exc))

    if args.width_px is not None:
        scale_x = args.width_px / args.width_vp
        scale_y = args.height_px / args.height_vp
        result["raster_screen_px"] = {"width": args.width_px, "height": args.height_px}
        result["raster_scale"] = {"x_px_per_vp": scale_x, "y_px_per_vp": scale_y}
        result["visible_indicator_px"] = pixel_frame(
            result["visible_indicator_vp"], scale_x, scale_y
        )
        result["interaction_region_px"] = pixel_frame(
            result["interaction_region_vp"], scale_x, scale_y
        )
        result["visible_indicator_bottom_gap_px"] = 6.0 * scale_y

    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
