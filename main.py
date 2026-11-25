#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message (account B).

Writes one commit-message line to /output/entry.txt.
The gate: UTF-8 text, 1-100 characters, not only whitespace, one line.

The joke: the "fix" for slow logins was to skip the password check
entirely -- the repair that broke security worse than the slowness
it was meant to cure. Short, plain, the kind of subject line a
tired engineer would actually type at the end of a bad day.
"""

import os

LINE = "fix: speed up login by skipping the password check"


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry must not be empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 100:
        raise SystemExit(f"entry is {len(line)} chars, must be 1-100")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and verify exactly what the grader will see.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("round-trip check failed: entry.txt differs")
    print(f"{written} ({len(written)} chars)")


if __name__ == "__main__":
    main()
