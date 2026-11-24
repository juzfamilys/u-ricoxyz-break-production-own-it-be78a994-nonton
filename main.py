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
    """Gate: single line, 1-199 characters, non-empty, non-whitespace-only."""
    assert isinstance(text, str), "entry must be a string"
    assert text.strip(), "entry must not be empty or whitespace-only"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 199, f"entry must be 1-199 chars, got {len(text)}"


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote /output/entry.txt ({len(ENTRY)} chars):")
    print(ENTRY)


if __name__ == "__main__":
    main()
