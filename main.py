#!/usr/bin/env python3
"""Entry generator: The Funniest Office Joke, Judged Head to Head.

Writes the single-line entry to /output/entry.txt.
Deterministic: identical bytes on every run. Stdlib only, no network.
"""

import os

# One line. Setup: a meeting called to cut meetings. Turn: it runs
# nearly an hour, and the "could've been an email" verdict arrives
# as a reply-all from inside the meeting itself.
ENTRY = (
    "I called a 15-minute meeting to cut meetings; "
    "47 minutes later, someone reply-all'd asking if it could've "
    "been an email."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
