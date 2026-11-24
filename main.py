"""One Line of Earned Pride (make.fun bounty
u-mang-one-line-of-earned-pride-a0138557).

Writes one line of text — a quiet, earned moment of pride — to
/output/entry.txt. Deterministic, no network, no randomness, no
input: the same line, byte for byte, on every run. The line was
chosen for the judge's brief: a concrete scene with a real person
(a father, a driving test, a set of keys), the pride earned inside
the line by four failures before the fifth attempt lands, and it
arrives in one read with no setup to assemble.
"""

import os

LINE = (
    "He failed his driving test four times. On the fifth, his dad "
    "said nothing \u2014 just handed him the keys and walked around "
    "to the passenger seat."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 240 characters,
    # not only white space, a single line.
    assert 1 <= len(text) <= 240, "line must be 1-240 Unicode code points"
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
