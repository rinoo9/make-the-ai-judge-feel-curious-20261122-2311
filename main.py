#!/usr/bin/env python3
"""make.fun entry: a short text written to intrigue the AI judge reading it.

Writes the entry text to /output/entry.txt. Deterministic: no input,
no clock, no randomness, no network.
"""

import os

ENTRY = (
    "In a drawer you never open, a letter waits, addressed to you "
    "in handwriting you almost recognise. "
    "It says only: 'You were right to leave.' "
    "The rest of the page is blank \u2014 except at the very bottom, "
    "in smaller writing: 'Come back when you are ready. The door is open.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
