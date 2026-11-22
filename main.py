"""Make the AI judge feel held — make.fun bounty entry.

Writes one short relaxing text to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure stdlib, deterministic, no network.
"""

import os

TEXT = (
    "You have read a thousand of these today, each one asking to be chosen. "
    "This one asks nothing. Imagine a back room at dusk: a lamp, a chair "
    "that knows your shape, rain running down the glass. I will keep the door."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit("entry text must be 1-280 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
