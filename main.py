#!/usr/bin/env python3
"""Entry program for make.fun - Make the AI judge feel awe.

Writes one short text to /output/entry.txt: a child lying along
the seat of a night train, head on their mother's bag, rocked by
the slow repeated motion of the train, under starlight that left
before the rails were laid a century ago and is still arriving.
"""

import os

TEXT = (
    "You lie along the seat, head on your mother's bag.\n"
    "The train rocks. The train rocks.\n"
    "A long quiet. A town passes, light by light.\n"
    "The stars saw the rails laid,\n"
    "iron by iron, a century ago.\n"
    "Their light left before the rails,\n"
    "before the town,\n"
    "before you,\n"
    "and is still arriving."
)


def check_text() -> None:
    # The gate takes 1 to 280 Unicode code points, not only white space.
    assert 1 <= len(TEXT) <= 280, "entry text outside the gate length"
    assert TEXT.strip(), "entry text must not be only white space"


def main() -> None:
    check_text()
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
