"""Absurd invention pitch: a TV remote that refuses to stay lost in the sofa.

Writes one sentence (1-220 chars) pitching the SofaSonar remote to
/output/entry.txt and prints the character count.
"""

import os

SENTENCE = (
    "The SofaSonar: a TV remote that, the instant it slips between the "
    "sofa cushions, puffs up like a startled pufferfish and honks until "
    "someone fishes it out."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)
    print(f"chars: {len(SENTENCE)}")


if __name__ == "__main__":
    main()
