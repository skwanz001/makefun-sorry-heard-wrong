"""Sorry, I Heard That Wrong — make.fun entry (program/v1, Python 3.13).

Writes one line (<=140 chars) to /output/entry.txt: the apology a smart
speaker gives its owner after mishearing them.

Strategy, in my own words: the judge weighs humour first, freshness
second, then how much the line sounds like the device itself. Generic
"oops, wrong song" lines all lose, so this entry is built on one vivid,
original escalation instead of a pun: a plausible mishearing
("goodnight" -> "goodbye forever") that the speaker has already acted on
(it told the owner's mother), landing on a concrete, warm image (a
casserole) that no other entry will have. The frame "Sorry, I heard X
as Y" is exactly how a smart speaker talks, so the device voice is
baked into the sentence rather than bolted on.
"""

import os

ENTRY = (
    "Sorry, I heard 'goodnight' as 'goodbye forever' and have already "
    "told your mother. She sends love and a casserole."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 140:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-140")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
