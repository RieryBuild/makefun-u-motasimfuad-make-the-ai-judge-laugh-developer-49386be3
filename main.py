"""Make the AI Judge Laugh: Developer Excuses.

The entry is one funny single-line excuse a developer gives when code
breaks in production. The chosen line turns the rollback — the safety
net every incident response reaches for — into the joke itself: the
"last good" deploy was broken too, and nobody had noticed. The twist
lands at the end, the jargon (rollback, deploy, last good) is used
exactly as a developer would say it out loud, and nothing in the line
can be trimmed without losing the laugh.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
exactly the line, with no trailing newline.
"""

import os

LINE = "The rollback failed because the last good deploy was broken too \u2014 we just hadn't noticed yet."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
