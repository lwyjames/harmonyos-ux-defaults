#!/usr/bin/env python3
"""Reject expanded Live View raster output that changes pixels outside its card mask."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare a card-free base frame with a card-present frame and require "
            "zero pixel changes outside the rounded card plus its antialias tolerance."
        )
    )
    parser.add_argument("base", type=Path)
    parser.add_argument("overlay", type=Path)
    parser.add_argument("--card-x-px", type=int, required=True)
    parser.add_argument("--card-y-px", type=int, required=True)
    parser.add_argument("--card-width-px", type=int, required=True)
    parser.add_argument("--card-height-px", type=int, required=True)
    parser.add_argument("--radius-px", type=int, required=True)
    parser.add_argument("--edge-tolerance-px", type=int, default=1)
    parser.add_argument("--channel-tolerance", type=int, default=0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    base = Image.open(args.base).convert("RGBA")
    overlay = Image.open(args.overlay).convert("RGBA")

    if base.size != overlay.size:
        print(json.dumps({"passed": False, "reason": "canvas-size-mismatch", "base": base.size, "overlay": overlay.size}))
        return 1

    if min(args.card_width_px, args.card_height_px, args.radius_px) <= 0:
        raise SystemExit("card dimensions and radius must be positive")
    if min(args.edge_tolerance_px, args.channel_tolerance) < 0:
        raise SystemExit("tolerances must be non-negative")

    width, height = base.size
    x0, y0 = args.card_x_px, args.card_y_px
    x1 = x0 + args.card_width_px - 1
    y1 = y0 + args.card_height_px - 1
    if x0 < 0 or y0 < 0 or x1 >= width or y1 >= height:
        raise SystemExit("rounded card frame must remain inside both canvases")

    protected = Image.new("L", base.size, 0)
    draw = ImageDraw.Draw(protected)
    draw.rounded_rectangle((x0, y0, x1, y1), radius=args.radius_px, fill=255)
    if args.edge_tolerance_px:
        protected = protected.filter(ImageFilter.MaxFilter(args.edge_tolerance_px * 2 + 1))

    difference = ImageChops.difference(base, overlay)
    channels = difference.split()
    max_channel = channels[0]
    for channel in channels[1:]:
        max_channel = ImageChops.lighter(max_channel, channel)
    changed = max_channel.point(lambda value: 255 if value > args.channel_tolerance else 0)
    outside = ImageChops.invert(protected)
    violations = ImageChops.multiply(changed, outside)
    histogram = violations.histogram()
    changed_outside = histogram[255]
    bbox = violations.getbbox()

    report = {
        "passed": changed_outside == 0,
        "canvas": {"width": width, "height": height},
        "card": {
            "x": x0,
            "y": y0,
            "width": args.card_width_px,
            "height": args.card_height_px,
            "radius": args.radius_px,
        },
        "edge_tolerance_px": args.edge_tolerance_px,
        "channel_tolerance": args.channel_tolerance,
        "changed_pixels_outside_protected_mask": changed_outside,
        "violation_bbox": bbox,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
