#!/usr/bin/env python3
"""soundex - Compute Soundex phonetic code for names."""
import sys

MAP = {"B":"1","F":"1","P":"1","V":"1","C":"2","G":"2","J":"2","K":"2","Q":"2","S":"2","X":"2","Z":"2","D":"3","T":"3","L":"4","M":"5","N":"5","R":"6"}

def soundex(name):
    name = "".join(c for c in name.upper() if c.isalpha())
    if not name: return ""
    code = [name[0]]
    prev = MAP.get(name[0], "0")
    for c in name[1:]:
        d = MAP.get(c, "0")
        if d != "0" and d != prev: code.append(d)
        if d != "0": prev = d
        else: prev = "0"
        if len(code) == 4: break
    return "".join(code).ljust(4, "0")

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: soundex <name> [name...]"); sys.exit(1)
    for n in sys.argv[1:]: print(f"{n}: {soundex(n)}")
