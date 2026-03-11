#!/usr/bin/env python3
"""Soundex — phonetic algorithm for indexing names by sound."""
import sys

MAP = {'B':'1','F':'1','P':'1','V':'1','C':'2','G':'2','J':'2','K':'2','Q':'2',
       'S':'2','X':'2','Z':'2','D':'3','T':'3','L':'4','M':'5','N':'5','R':'6'}

def soundex(name):
    name = name.upper().strip()
    if not name: return ""
    code = [name[0]]
    prev = MAP.get(name[0], '0')
    for c in name[1:]:
        digit = MAP.get(c, '0')
        if digit != '0' and digit != prev:
            code.append(digit)
        prev = digit if digit != '0' else prev
    return ("".join(code) + "000")[:4]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        pairs = [("Robert","Rupert"),("Smith","Smythe"),("Johnson","Jonson"),("Ashcraft","Ashcroft")]
        for a, b in pairs:
            print(f"  {a}={soundex(a)}  {b}={soundex(b)}  match={soundex(a)==soundex(b)}")
    else:
        for name in sys.argv[1:]:
            print(f"{name} → {soundex(name)}")
