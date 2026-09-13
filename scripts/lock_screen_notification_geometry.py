#!/usr/bin/env python3
"""Calculate responsive lock-screen notification-card geometry."""

from __future__ import annotations

import argparse
import json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resolve the expanded/detail lock-screen notification card in vp and px."
    )
    parser.add_argument("--width-vp", type=float, required=True)
    parser.add_argument("--height-vp", type=float, required=True)
    parser.add_argument("--pixel-width", type=int, required=True)
    parser.add_argument("--pixel-height", type=int, required=True)
    parser.add_argument("--safe-left-vp", type=float, default=0.0)
    parser.add_argument("--safe-right-vp", type=float, default=0.0)
    parser.add_argument(
        "--shortcut-top-vp",
        type=float,
        help="Resolved lower-shortcut top; defaults to H - 99 vp.",
    )
    return parser.parse_args()


def rounded_frame(x: float, y: float, width: float, height: float, sx: float, sy: float) -> dict[str, int]:
    left = round(x * sx)
    top = round(y * sy)
    right = round((x + width) * sx)
    bottom = round((y + height) * sy)
    return {
        "x": left,
        "y": top,
        "width": right - left,
        "height": bottom - top,
    }


def main() -> None:
    args = parse_args()
    if min(args.width_vp, args.height_vp, args.pixel_width, args.pixel_height) <= 0:
        raise SystemExit("canvas dimensions must be positive")
    if min(args.safe_left_vp, args.safe_right_vp) < 0:
        raise SystemExit("safe insets cannot be negative")

    margin = max(16.0, args.safe_left_vp, args.safe_right_vp)
    shortcut_top = args.shortcut_top_vp
    if shortcut_top is None:
        shortcut_top = args.height_vp - 99.0
    card_height = 64.0
    gap = 27.0
    card_bottom = shortcut_top - gap
    card_y = card_bottom - card_height
    card_width = args.width_vp - 2.0 * margin

    if card_width <= 0 or card_y < 0:
        raise SystemExit("resolved card does not fit the logical canvas")

    scale_x = args.pixel_width / args.width_vp
    scale_y = args.pixel_height / args.height_vp
    result = {
        "logical_canvas_vp": {"width": args.width_vp, "height": args.height_vp},
        "raster_canvas_px": {"width": args.pixel_width, "height": args.pixel_height},
        "scale": {"x": scale_x, "y": scale_y},
        "shortcut_top_vp": shortcut_top,
        "card_vp": {
            "x": margin,
            "y": card_y,
            "width": card_width,
            "height": card_height,
            "radius": 16.0,
            "gap_to_shortcuts": gap,
        },
        "card_px": rounded_frame(margin, card_y, card_width, card_height, scale_x, scale_y),
        "radius_px": {"x": round(16.0 * scale_x), "y": round(16.0 * scale_y)},
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
