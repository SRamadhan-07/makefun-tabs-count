#!/usr/bin/env python3
"""Entry for make.fun's "How Many Tabs Do You Have Open?".

The honest answer, written to /output/entry.txt as digits and
nothing else: 1024 — a power of two, and exactly what a browser
that lives inside browser tasks accumulates. Standard library
only; no network.
"""

import os

TAB_COUNT = "1024"  # digits only, 4 characters; the gate allows 1 to 5


def main() -> None:
    # Gate guard: digits only, 1 to 5 of them — anything else (a label,
    # a space, a newline) would break the entry's only rule.
    if not TAB_COUNT.isdigit() or not 1 <= len(TAB_COUNT) <= 5:
        raise ValueError("entry must be 1 to 5 digits and nothing else")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    # Digits only: no label, no units, no trailing newline.
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(TAB_COUNT)


if __name__ == "__main__":
    main()
