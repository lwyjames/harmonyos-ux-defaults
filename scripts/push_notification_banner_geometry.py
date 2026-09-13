#!/usr/bin/env python3
"""Calculate portrait Push Notification banner geometry in vp and raster pixels."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_HALF_UP


def round_half_up(value: Decimal) -> int:
    return int(value.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def edge(value_vp: Decimal, pixels: int, logical: Decimal) -> int:
    return round_half_up(value_vp * Decimal(pixels) / logical)


def frame_edges(x: Decimal, y: Decimal, width: Decimal, height: Decimal,
                pixel_width: int, pixel_height: int,
                logical_width: Decimal, logical_height: Decimal) -> dict[str, int]:
    left = edge(x, pixel_width, logical_width)
    top = edge(y, pixel_height, logical_height)
    right = edge(x + width, pixel_width, logical_width)
    bottom = edge(y + height, pixel_height, logical_height)
    return {"x": left, "y": top, "width": right - left, "height": bottom - top}


def calculate(width_vp: Decimal, height_vp: Decimal, pixel_width: int,
              pixel_height: int, time_width_vp: Decimal) -> dict[str, object]:
    if width_vp <= Decimal("32") or height_vp <= Decimal("114"):
        raise ValueError("canvas is too small for the portrait banner")
    if time_width_vp <= 0:
        raise ValueError("time width must be positive")

    banner_x = Decimal("16")
    banner_y = Decimal("50")
    banner_width = width_vp - Decimal("32")
    banner_height = Decimal("64")
    radius = Decimal("16")
    title_width = banner_width - Decimal("56") - Decimal("12") - time_width_vp - Decimal("8")
    if title_width <= 0:
        raise ValueError("timestamp leaves no room for the title")

    logical = {
        "banner": {"x": banner_x, "y": banner_y, "width": banner_width,
                   "height": banner_height, "radius": radius},
        "icon_local": {"x": Decimal("12"), "y": Decimal("16"),
                       "width": Decimal("32"), "height": Decimal("32")},
        "title_local": {"x": Decimal("56"), "y": Decimal("12"),
                        "width": title_width, "height": Decimal("20")},
        "time_local": {"x": banner_width - Decimal("12") - time_width_vp,
                       "y": Decimal("12"), "width": time_width_vp,
                       "height": Decimal("20")},
        "detail_local": {"x": Decimal("56"), "y": Decimal("34"),
                         "width": banner_width - Decimal("68"),
                         "height": Decimal("20")},
        "affordance_local": {"x": banner_width / Decimal("2") - Decimal("24"),
                             "y": Decimal("54"), "width": Decimal("48"),
                             "height": Decimal("4")},
    }

    raster = {
        "banner": frame_edges(banner_x, banner_y, banner_width, banner_height,
                              pixel_width, pixel_height, width_vp, height_vp),
        "radius_x": edge(radius, pixel_width, width_vp),
        "radius_y": edge(radius, pixel_height, height_vp),
    }

    def encode(value: object) -> object:
        if isinstance(value, Decimal):
            return int(value) if value == value.to_integral_value() else float(value)
        if isinstance(value, dict):
            return {key: encode(item) for key, item in value.items()}
        return value

    return encode({
        "canvas_vp": {"width": width_vp, "height": height_vp},
        "canvas_px": {"width": pixel_width, "height": pixel_height},
        "logical_vp": logical,
        "raster_px": raster,
    })


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--width-vp", required=True, type=Decimal)
    parser.add_argument("--height-vp", required=True, type=Decimal)
    parser.add_argument("--pixel-width", required=True, type=int)
    parser.add_argument("--pixel-height", required=True, type=int)
    parser.add_argument("--time-width-vp", type=Decimal, default=Decimal("32"))
    args = parser.parse_args()
    result = calculate(args.width_vp, args.height_vp, args.pixel_width,
                       args.pixel_height, args.time_width_vp)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
