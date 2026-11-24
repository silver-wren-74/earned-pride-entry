#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun bounty entry.

Writes a single original line (1 to 240 characters) to /output/entry.txt,
exactly as the competition gate expects: a quiet, earned moment of pride
for someone in a scene.
"""

import os

# REVISION PASS (against the RULES judging criteria, in order):
# 1. Genuine earned pride: thirty years of sweeping + teaching the girl is
#    the long effort; the pride lands quietly, never asserted.
# 2. Concrete scene, real person: a named man, a gym floor, a buzzer-beater.
# 3. Pride earned inside the line by effort the reader can feel.
# 4. Lands in one read: the final clause arrives with the last words.
# 5. Freshness: a janitor's pride, not a trophy, podium or graduation.
#    The nurse-and-baby draft was cut for being a familiar image.
LINE = (
    "After thirty years sweeping the same gym floor, old Mr. Adi watched "
    "the girl he taught to dribble in socks sink the buzzer-beater \u2014 "
    "and kept sweeping, smiling."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"line must be 1-240 chars, got {len(text)}"
    # Single line, no trailing newline: the gate counts the file's characters.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
