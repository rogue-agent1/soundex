#!/usr/bin/env python3
"""soundex - Soundex phonetic encoding algorithm."""
import argparse

SOUNDEX_MAP = {c: d for chars, d in [
    ("BFPV", "1"), ("CGJKQSXZ", "2"), ("DT", "3"),
    ("L", "4"), ("MN", "5"), ("R", "6")
] for c in chars}

def soundex(name: str) -> str:
    name = name.upper().strip()
    if not name: return ""
    result = [name[0]]
    prev = SOUNDEX_MAP.get(name[0], "0")
    for c in name[1:]:
        code = SOUNDEX_MAP.get(c, "0")
        if code != "0" and code != prev:
            result.append(code)
        if c not in "HW":
            prev = code
    return "".join(result)[:4].ljust(4, "0")

def main():
    p = argparse.ArgumentParser(description="Soundex encoding")
    p.add_argument("names", nargs="+")
    p.add_argument("-c", "--compare", action="store_true", help="Compare pairs")
    args = p.parse_args()
    if args.compare and len(args.names) >= 2:
        s1, s2 = soundex(args.names[0]), soundex(args.names[1])
        print(f"{args.names[0]} -> {s1}")
        print(f"{args.names[1]} -> {s2}")
        print(f"Match: {s1 == s2}")
    else:
        for name in args.names:
            print(f"{name} -> {soundex(name)}")

if __name__ == "__main__":
    main()
