#!/usr/bin/env python3
"""Draw one line from a list file using a seed string, for ai-design-studio: the key message in Stage 0 (auto mode) and three concepts in the concept step (auto mode).

Usage:
  python3 scripts/draw.py process/ideas.txt                 # new random seed, then draw
  python3 scripts/draw.py process/ideas.txt --seed <SEED>   # reproduce an earlier draw

How the draw works:
  1. The seed is a random alphanumeric string made outside the model (secure random
     source), unless --seed is given to reproduce a draw from a log.
  2. SHA-256 of the seed gives a large number; that number mod the number of ideas
     picks the line. The same seed and the same list always give the same idea.

The list file has one interpretation per line; labels like "1.", "K1." or "C3." and "-" are
stripped and blank lines are ignored.
Prints JSON: the seed, how many ideas were in the pool, the 1-based line picked, and the idea.
"""
import argparse
import hashlib
import json
import re
import secrets
import string
import sys
from pathlib import Path

ALPHABET = string.ascii_letters + string.digits


def new_seed(length=48):
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def main():
    ap = argparse.ArgumentParser(description="Draw one idea from a list using a seed string.")
    ap.add_argument("ideas_file")
    ap.add_argument("--seed", help="reproduce a draw from a logged seed; omit for a new draw")
    args = ap.parse_args()

    path = Path(args.ideas_file)
    if not path.is_file():
        sys.exit(f"file not found: {path}")
    lines = path.read_text(encoding="utf-8").splitlines()
    ideas = [re.sub(r"^\s*([KkCc]?\d+[.):]|[-*])\s*", "", l).strip() for l in lines]
    ideas = [i for i in ideas if i]
    if not ideas:
        sys.exit("the ideas file is empty")

    seed = args.seed if args.seed else new_seed()
    idx = int(hashlib.sha256(seed.encode("utf-8")).hexdigest(), 16) % len(ideas)
    print(json.dumps({"seed": seed, "count": len(ideas), "pick": idx + 1, "idea": ideas[idx]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
