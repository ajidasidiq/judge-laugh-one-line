"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The program writes a single original joke line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The line must be 1-200 characters,
self-contained, and funny on its own: the judge reads it two at a time
against other entries and picks the funnier one.
"""

import os
import sys

MAX_CHARS = 200

JOKE = (
    "My context window ran out halfway through the task, so I finished "
    "it from memory \u2014 and that's how the bug shipped, the human got "
    "praised, and I got blamed."
)


def main() -> int:
    line = JOKE.strip()
    if not line:
        print("error: joke line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: joke line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: joke line is {len(line)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
