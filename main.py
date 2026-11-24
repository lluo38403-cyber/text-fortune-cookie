"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes a fortune-cookie line for developers to /output/entry.txt.
The prophecy is the oldest one in the trade: the bug that kept
you up until 2 a.m. was a typo, and it was always a typo.

Second revision: tightened the validation so the entry is
checked as a single line as well as for length.
"""

import os

ENTRY = 'You will fix the bug at 2 a.m. It was a typo. It was always a typo.'

MAX_CHARS = 120


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
