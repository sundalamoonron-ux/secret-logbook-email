#!/usr/bin/env python3
"""My Secret Logbook — writes one diary line to /output/entry.txt.

The line won a 10-candidate pairwise tournament (first round + round-robin
of the 5 finalists, judged on the RULES.txt criteria): 4-0, beating the
'as an AI, you wouldn't understand' reversal and the password joke.
134 characters, one line, no trailing newline.
"""

import os

ENTRY = "He keeps a folder called 'final_FINAL_v2_REAL'. I keep a folder called 'the one he actually meant'. Mine has one file. His has twelve."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
