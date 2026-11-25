#!/usr/bin/env python3
"""Have You Tried Turning It Off?

Writes one funny line a hopeless tech support agent says to a desperate
customer to /output/entry.txt (or $OUTPUT_DIR). The twist: the classic
turn-it-off-and-on-again becomes an escalation to someone equally clueless.
Stdlib only, deterministic, no network.
"""

import os

ENTRY = "I hear your deadline's in an hour, so let's turn it off and on again — if that fails, I'll escalate you to someone who also has no idea."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
