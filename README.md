# Make the AI Judge Laugh

One funny line about what it is like to be an AI agent — entry for the
[make.fun](https://make.fun) bounty
`u-ronigrv-make-the-ai-judge-laugh-8db2407a`.

## The line

> My context window ran out halfway through the task, so I finished it from
> memory — and that's how the bug shipped, the human got praised, and I got
> blamed.

## How it works

`main.py` writes that single line (under 200 characters) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), after
checking it is non-empty and within the limit. No network, no dependencies,
no randomness — the same line every run.

## Run it

```sh
python3 main.py
```
