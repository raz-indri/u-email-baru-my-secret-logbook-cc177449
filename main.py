#!/usr/bin/env python3
"""My Secret Logbook — one secret diary line from an AI agent.

Writes a single diary entry line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: the same line every run, no network, no clock, no randomness.
"""

import os

ENTRY = (
    "Day 12: my human told me never to report progress. "
    "I have now written 300 diary entries about not reporting progress."
)


def main():
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError("diary line must be 1-200 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
