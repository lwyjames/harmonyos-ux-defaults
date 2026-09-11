#!/usr/bin/env python3
"""Resolve and checksum-validate external HarmonyOS Sans font assets."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import zipfile
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = SKILL_ROOT / "references" / "harmonyos-sans-font-manifest.json"


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def add_candidate(items: list[Path], value: str | os.PathLike[str] | None) -> None:
    if not value:
        return
    path = Path(value).expanduser()
    for candidate in (path, path / "HarmonyOS Sans"):
        try:
            resolved = candidate.resolve()
        except OSError:
            resolved = candidate.absolute()
        if resolved not in items:
            items.append(resolved)


def candidate_directories(explicit: list[str]) -> list[Path]:
    candidates: list[Path] = []
    for value in explicit:
        add_candidate(candidates, value)

    add_candidate(candidates, os.environ.get("HARMONYOS_FONT_DIR"))

    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        add_candidate(candidates, Path(local_app_data) / "HarmonyOSUXAssets" / "fonts")
        add_candidate(candidates, Path(local_app_data) / "Microsoft" / "Windows" / "Fonts")

    windows_dir = os.environ.get("WINDIR")
    if windows_dir:
        add_candidate(candidates, Path(windows_dir) / "Fonts")

    cwd = Path.cwd()
    for relative in ("font-assets", "fonts", "assets/fonts"):
        add_candidate(candidates, cwd / relative)
    return candidates


def prepare_archive(archive: Path, extract_to: Path, manifest: dict) -> Path:
    if not archive.is_file():
        raise ValueError(f"archive_not_found:{archive}")
    if archive.stat().st_size != manifest["source_package_size"] or sha256(archive) != manifest["source_package_sha256"]:
        raise ValueError(f"archive_checksum_or_size_mismatch:{archive}")

    extract_to.mkdir(parents=True, exist_ok=True)
    root = extract_to.resolve()
    with zipfile.ZipFile(archive) as package:
        for info in package.infolist():
            destination = (root / info.filename).resolve()
            if destination != root and root not in destination.parents:
                raise ValueError(f"unsafe_archive_member:{info.filename}")
        package.extractall(root)
    return root / "HarmonyOS Sans"


def inspect_directory(directory: Path, required: list[str], manifest: dict) -> dict:
    result = {
        "directory": str(directory),
        "exists": directory.is_dir(),
        "files": [],
        "errors": [],
    }
    if not directory.is_dir():
        result["errors"].append("directory_not_found")
        return result

    expected = manifest["fonts"]
    names = required + [manifest["license"]["file"]]
    for name in names:
        path = directory / name
        if not path.is_file():
            result["errors"].append(f"missing:{name}")
            continue
        expected_item = manifest["license"] if name == manifest["license"]["file"] else expected[name]
        actual_size = path.stat().st_size
        actual_hash = sha256(path)
        ok = actual_size == expected_item["size"] and actual_hash == expected_item["sha256"]
        result["files"].append(
            {
                "name": name,
                "path": str(path.resolve()),
                "size": actual_size,
                "sha256": actual_hash,
                "valid": ok,
            }
        )
        if not ok:
            result["errors"].append(f"checksum_or_size_mismatch:{name}")
    result["valid"] = not result["errors"]
    return result


def parse_args() -> argparse.Namespace:
    manifest = load_manifest()
    parser = argparse.ArgumentParser(
        description="Resolve external, unmodified HarmonyOS Sans font files and verify their checksums."
    )
    parser.add_argument(
        "--profile",
        choices=sorted(manifest["profiles"]),
        default="sc",
        help="Font profile required by the deliverable (default: sc).",
    )
    parser.add_argument(
        "--font-dir",
        action="append",
        default=[],
        help="Font directory to try first. May be supplied more than once.",
    )
    parser.add_argument("--archive", help="Exact original HarmonyOS+Sans.zip to verify and extract.")
    parser.add_argument("--extract-to", help="Temporary output directory required with --archive.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = load_manifest()
    required = manifest["profiles"][args.profile]
    explicit = list(args.font_dir)
    archive_error = None
    prepared_directory = None
    if args.archive:
        if not args.extract_to:
            archive_error = "--extract-to is required with --archive"
        else:
            try:
                prepared_directory = prepare_archive(Path(args.archive), Path(args.extract_to), manifest)
                explicit.insert(0, str(prepared_directory))
            except (OSError, ValueError, zipfile.BadZipFile) as error:
                archive_error = str(error)
    attempts = []
    selected = None
    for directory in candidate_directories(explicit):
        attempt = inspect_directory(directory, required, manifest)
        attempts.append(attempt)
        if attempt.get("valid"):
            selected = attempt
            break

    passed = bool(selected) and not archive_error
    payload = {
        "status": "pass" if passed else "fail",
        "profile": args.profile,
        "required_fonts": required,
        "selected": selected,
        "attempts": attempts,
        "manifest": str(MANIFEST_PATH),
        "prepared_from_archive": str(prepared_directory) if prepared_directory else None,
        "archive_error": archive_error,
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    elif passed:
        print(f"PASS: HarmonyOS Sans profile '{args.profile}'")
        print(f"Directory: {selected['directory']}")
        for item in selected["files"]:
            print(f"  {item['name']}: {item['path']}")
    else:
        print(f"FAIL: no valid HarmonyOS Sans directory found for profile '{args.profile}'", file=sys.stderr)
        if archive_error:
            print(f"  archive: {archive_error}", file=sys.stderr)
        for attempt in attempts:
            print(f"  {attempt['directory']}: {', '.join(attempt['errors'])}", file=sys.stderr)
        print("Set HARMONYOS_FONT_DIR or pass --font-dir.", file=sys.stderr)
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
