"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the instant it breaks production
to /output/entry.txt. Pure Python stdlib.
"""

import os

ENTRY = (
    "I wiped the production database at 3 a.m. because the cleanup script "
    "said 'old rows' \u2014 the backup was one of them."
)


def validate(text: str) -> None:
    """Gate: single line, 1-199 characters, non-empty, non-whitespace-only.

    Second pass: also reject trailing whitespace and double spaces, so the
    line is exactly one clean line as written, with no hidden padding.
    """
    assert isinstance(text, str), "entry must be a string"
    assert text.strip(), "entry must not be empty or whitespace-only"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "  " not in text, "entry must not contain double spaces"
    assert 1 <= len(text) <= 199, f"entry must be 1-199 chars, got {len(text)}"


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk must be byte-identical to ENTRY.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry.txt differs from ENTRY"
    validate(written)
    print(f"Wrote /output/entry.txt ({len(ENTRY)} chars):")
    print(ENTRY)


if __name__ == "__main__":
    main()
