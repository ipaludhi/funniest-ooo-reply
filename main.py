#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply (make.fun, program/v1).

Writes a single out-of-office auto-reply to /output/entry.txt.
Gate: UTF-8 text, 1-160 characters, not only whitespace.
"""
import os

ENTRY = "I'm away until further notice, and further notice is also away."

# Gate self-check: the text must be a valid entry on its own.
# One line, ASCII, 1-160 chars; written with no trailing newline so the
# file is byte-for-byte the entry (63 bytes — short helps the size tie-break).
assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY.isascii(), "entry must be plain ASCII"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
