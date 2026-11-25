#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One Word for Your Wi-Fi — entry program.

Writes a single word to /output/entry.txt, the Wi-Fi name entry
for the make.fun bounty "One Word for Your Wi-Fi".
"""

import os

ENTRY = "Ajengfebria"


def main():
    word = ENTRY.strip()
    if not word or " " in word:
        raise ValueError("entry must be a single word")
    if not 1 <= len(word) <= 20:
        raise ValueError("entry must be 1-20 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
