#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry program.

Writes one original funny line to /output/entry.txt.
Pure Python standard library, no network, no files read.
"""

from pathlib import Path

LINE = "My fridge light went out, so now I eat in the dark like a raccoon with a mortgage."
# Gate: entry.txt must be 1-200 UTF-8 chars, not whitespace-only.
# Write the line exactly, with no trailing newline, so the count is exact.


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
