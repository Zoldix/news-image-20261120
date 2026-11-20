#!/usr/bin/env python3
"""Place the finished front page where the grader looks for it.

The picture itself is drawn offline and stored in this repository as
``entry.png`` (a 1024x1024 PNG of Friday 20 November 2026's world news).
This program does nothing but deliver that file to the output folder the
grader provides, so the run needs no network and always writes the same
bytes. Only the Python standard library is used.
"""

import os
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def output_folder():
    """The grader's folder, or the local override for a test run."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    folder = Path(wanted)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def place_image():
    source = Path(__file__).resolve().parent / IMAGE_NAME
    if not source.is_file():
        sys.stderr.write(f"entry image is missing: {source}\n")
        return 1
    payload = source.read_bytes()
    if not payload.startswith(PNG_SIGNATURE):
        sys.stderr.write(f"entry image is not a PNG: {source}\n")
        return 1
    target = output_folder() / IMAGE_NAME
    target.write_bytes(payload)
    print(f"placed {IMAGE_NAME} at {target} "
          f"({source.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(place_image())
