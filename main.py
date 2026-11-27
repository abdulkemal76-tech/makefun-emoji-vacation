"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt: Mount Fuji (U+1F5FB).

Why Fuji: the judge picks the emoji that most makes a stranger want to
book the flight. Fuji is a mountain *and* a faraway place — both named in
the judge's own first criterion — and it is one concrete, named dream
(Japan at dawn) instead of any generic holiday. It reads instantly at any
size, and at 4 UTF-8 bytes it also wins the size tie-break against longer
picks. No trailing newline: the file holds the emoji and nothing else.
"""

import os

# Mount Fuji, U+1F5FB — a single emoji, 4 bytes in UTF-8.
EMOJI = "\U0001F5FB"

# Guard the entry at import time: the bounty wants exactly ONE emoji.
# A single code point in the emoji ranges keeps the gate (1-8 chars) and
# the judge's first criterion ("is exactly one emoji") satisfied.
if len(EMOJI) != 1 or not (0x1F000 <= ord(EMOJI) <= 0x1FAFF):
    raise ValueError(f"EMOJI must be exactly one emoji code point, got {EMOJI!r}")

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Self-check: the file must hold exactly this one emoji, nothing else.
    # The gate allows 1-8 characters; we write exactly 1, with no newline,
    # so the entry also wins the byte-count tie-break.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != EMOJI:
        raise SystemExit(f"entry.txt mismatch: {written!r} != {EMOJI!r}")
    print(f"wrote {EMOJI} ({len(EMOJI.encode('utf-8'))} bytes) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
