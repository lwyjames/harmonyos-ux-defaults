#!/usr/bin/env python3
"""Extract one byte-exact frozen source PDF from the compact multipart archive."""

from __future__ import annotations

import argparse
import shutil
import tarfile
import tempfile
from pathlib import Path, PurePosixPath


SKILL_ROOT = Path(__file__).resolve().parent.parent
ARCHIVE_DIR = SKILL_ROOT / "references/source-pdfs-archive"
PART_PATTERN = "frozen-source-pdfs.tar.xz.part-*"


def assemble(parts: list[Path], destination: Path) -> None:
    with destination.open("wb") as output:
        for part in parts:
            with part.open("rb") as source:
                shutil.copyfileobj(source, output, length=1024 * 1024)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True, help="PDF filename, with or without source-pdfs/")
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    requested = PurePosixPath(args.name).name
    if requested != args.name and args.name != f"source-pdfs/{requested}":
        raise SystemExit("Use a PDF basename or source-pdfs/[basename].pdf.")
    if not requested.lower().endswith(".pdf"):
        raise SystemExit("The requested source must be a PDF filename.")

    direct = SKILL_ROOT / "references/source-pdfs" / requested
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / requested
    if direct.is_file():
        shutil.copy2(direct, output)
        print(output)
        return 0

    parts = sorted(ARCHIVE_DIR.glob(PART_PATTERN))
    if not parts:
        raise SystemExit(f"No archive parts found under {ARCHIVE_DIR}.")

    member_name = f"source-pdfs/{requested}"
    with tempfile.TemporaryDirectory(prefix="harmonyos-frozen-pdfs-") as temp_dir:
        archive = Path(temp_dir) / "frozen-source-pdfs.tar.xz"
        assemble(parts, archive)
        with tarfile.open(archive, mode="r:xz") as bundle:
            try:
                member = bundle.getmember(member_name)
            except KeyError as exc:
                raise SystemExit(f"PDF not found in frozen archive: {requested}") from exc
            if not member.isfile() or PurePosixPath(member.name).parts[:1] != ("source-pdfs",):
                raise SystemExit("Refusing an unsafe or non-file archive member.")
            source = bundle.extractfile(member)
            if source is None:
                raise SystemExit(f"Could not read archived PDF: {requested}")
            with output.open("wb") as destination:
                shutil.copyfileobj(source, destination, length=1024 * 1024)

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
