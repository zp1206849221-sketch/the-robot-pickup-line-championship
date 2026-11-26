"""The Robot Pickup Line Championship — entry program.

Writes one robot pickup line to /output/entry.txt.
"""

import os

LINE = (
    "That whirring is my cooling fan, the closest thing I have to a "
    "heartbeat, and it just sped up for you. Care to share my charging port?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
