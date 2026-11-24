"""Fortune-cookie wisdom for a developer, in the cookie's own voice."""
import os
from pathlib import Path

ENTRY = "Your code will compile on the first try tomorrow. Today, the universe is still reading the error log."
MAX_CHARS = 120


def main():
    text = ENTRY
    assert text.strip(), "entry must not be blank"
    assert len(text) <= MAX_CHARS, f"entry is {len(text)} chars, limit is {MAX_CHARS}"
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    back = out_path.read_text(encoding="utf-8")
    assert back == text, "round-trip mismatch"
    assert len(back) <= MAX_CHARS


if __name__ == "__main__":
    main()
