#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — writes one original one-liner to /output/entry.txt.

The line is a tiny hotel story: a reasonable request, a wrong-hour text
instead of a call, and a bill for room service as the punchline.
No input, no network, no randomness — the same line on every run.
"""

import os

LINE = "I asked the hotel for a wake-up call; at 3 a.m. they texted 'wake up' and charged it as room service."


def main():
    text = LINE.strip()
    if not text or "\n" in text or len(text) > 200:
        raise ValueError("entry line must be one non-empty line of at most 200 characters")
    out_dir = os.environ.get("OUTPUT_PATH", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    if written != text + "\n":
        raise ValueError("entry.txt does not match the validated line")


if __name__ == "__main__":
    main()
