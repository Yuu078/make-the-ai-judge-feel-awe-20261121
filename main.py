#!/usr/bin/env python3
"""Entry program for make.fun - Make the AI judge feel awe.

Writes one short text to /output/entry.txt: a child lying on a
roof at night with their head resting on their father's arm,
feeling his chest rise and fall under them while the tiles give
the day's warmth back to the dark, and overhead the slow wheel
of stars turns as it once turned over empty sea and nameless
hills, carrying the house and carrying them both.
"""

import os

LINES = [
    "You lie on the roof, head on your father's arm.",
    "His chest rises. His chest falls.",
    "The clay tiles give their warmth back to the dark.",
    "Overhead, the slow wheel of stars turns",
    "as it turned over empty sea,",
    "over nameless hills,",
    "carrying the house,",
    "carrying you both.",
]

ENTRY_TEXT = "\n".join(LINES)


def validate(text: str) -> None:
    # The gate accepts 1 to 280 Unicode code points of real text.
    points = len(text)
    assert 1 <= points <= 280, f"entry text has {points} code points"
    assert text.strip(), "entry text must not be only white space"


def write_entry() -> str:
    validate(ENTRY_TEXT)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)
    return target


if __name__ == "__main__":
    write_entry()
