#!/usr/bin/env python3
"""Materialize a pixel-verified PNG from a compact lossless home-screen master."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from PIL import Image


SKILL_ROOT = Path(__file__).resolve().parent.parent
MASTERS = {
    "pura-x-max-unfolded-portrait": {
        "file": "pura-x-max-unfolded-portrait.lossless.webp",
        "size": (2194, 3101),
        "rgb_sha256": "93fcaf0c1b2a6f2df5fbb46f46bd9dd074b589ba5043c78291c3301454a4640a",
    },
    "pura-x-view-front": {
        "file": "pura-x-view-front.lossless.webp",
        "size": (2376, 4018),
        "rgb_sha256": "9743c8f83f97f74c4feb049782ba8c41bfeb24d41adaea18754d24aa8cf5e944",
    },
    "pura-90-pro-max-portrait": {
        "file": "pura-90-pro-max-portrait.lossless.webp",
        "size": (1831, 4032),
        "rgb_sha256": "cd8183ff9a3a0a0ba495a7dbbc7e85cada0f05900d8f75f2a6b7ee19f0b53a2a",
    },
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--device", required=True, choices=sorted(MASTERS))
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    mapping = MASTERS[args.device]
    source = SKILL_ROOT / "assets/default-homescreens" / mapping["file"]
    with Image.open(source) as image:
        decoded = image.convert("RGB")

    if decoded.size != mapping["size"]:
        raise SystemExit(
            f"Size verification failed: expected {mapping['size']}, got {decoded.size}."
        )
    digest = hashlib.sha256(decoded.tobytes()).hexdigest()
    if digest != mapping["rgb_sha256"]:
        raise SystemExit(
            f"Pixel verification failed: expected {mapping['rgb_sha256']}, got {digest}."
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    decoded.save(args.output, format="PNG", optimize=True, compress_level=9)
    print(f"PASS {args.device}: {decoded.width}x{decoded.height}, RGB SHA-256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
