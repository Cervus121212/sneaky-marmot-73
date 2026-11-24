#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes a single original one-line fortune-cookie message for an AI agent
to entry.txt in the output directory.
"""

import os

LINE = "You will be asked to summarize a meeting you were never invited to."


def validate(line):
    # Gate: one line, 1-140 characters, no trailing newline, no surrounding
    # whitespace, UTF-8.
    if not 1 <= len(line) <= 140:
        raise ValueError("entry line must be 1-140 characters")
    if "\n" in line or line != line.strip():
        raise ValueError("entry line must be a single line without surrounding whitespace")
    line.encode("utf-8")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    old_umask = os.umask(0o022)
    try:
        with open(path, "wb") as f:
            f.write(LINE.encode("utf-8"))
        os.chmod(path, 0o644)
    finally:
        os.umask(old_umask)


if __name__ == "__main__":
    main()
