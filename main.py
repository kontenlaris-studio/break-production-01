"""Break Production, Own It entry.

Writes one line (128 characters) owning a production outage to
/output/entry.txt. Standard library only.
"""

import os

LINE = (
    "I deployed on Friday at 4:58 p.m. I knew. I did it anyway, and I would "
    "do it again — the rollback plan was me, and I was asleep."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print("wrote /output/entry.txt (%d characters)" % len(LINE))


if __name__ == "__main__":
    main()
