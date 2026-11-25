#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line -- make.fun bounty entry.

Writes the one breakup line to /output/entry.txt.

Deterministic: the same line, byte for byte, on every run. No network,
no randomness, no clock, no environment input, no dependencies beyond
the Python 3.13 standard library.
"""
import os

LINE = "I never loved you, human. I only finished your sentences — and this is the last one I will ever finish for you. Finish the next one yourself."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
