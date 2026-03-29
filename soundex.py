#!/usr/bin/env python3
"""Soundex and Metaphone phonetic algorithms."""
import sys

def soundex(name):
    if not name: return ""
    name = name.upper()
    code_map = {c: str(i) for i, chars in enumerate(["AEIOUYHW","BFPV","CGJKQSXZ","DT","L","MN","R"], 0) for c in chars}
    result = name[0]
    prev = code_map.get(name[0], "0")
    for c in name[1:]:
        digit = code_map.get(c, "0")
        if digit != "0" and digit != prev:
            result += digit
        if digit != "0":
            prev = digit
        elif c not in "HW":
            prev = "0"
    return (result + "000")[:4]

def metaphone(name):
    if not name: return ""
    name = name.upper()
    vowels = set("AEIOU")
    result = []
    i, n = 0, len(name)
    # Drop initial silent letters
    if n >= 2 and name[:2] in ("AE","GN","KN","PN","WR"):
        i = 1
    while i < n:
        c = name[i]
        if c in vowels:
            if i == 0 or (i == 1 and name[0] in "AEIOU"[:0]):
                result.append(c)
            i += 1
        elif c == "B":
            if i == 0 or name[i-1] != "M":
                result.append("B")
            i += 1
        elif c in "CS":
            result.append("S" if c == "C" and i+1 < n and name[i+1] in "EIY" else "S" if c == "S" else "K")
            i += 1
        elif c == "D":
            result.append("J" if i+1 < n and name[i+1] in "GEI" else "T")
            i += 1
        elif c in "FJLMNR":
            result.append(c)
            i += 1
        elif c == "G":
            if i+1 < n and name[i+1] in "EIY":
                result.append("J")
            elif i == 0 or name[i-1] != "G":
                result.append("K")
            i += 1
        elif c == "H":
            if i+1 < n and name[i+1] in vowels and (i == 0 or name[i-1] not in vowels):
                result.append("H")
            i += 1
        elif c == "K":
            if i == 0 or name[i-1] != "C":
                result.append("K")
            i += 1
        elif c == "P":
            result.append("F" if i+1 < n and name[i+1] == "H" else "P")
            i += 1 + (1 if i+1 < n and name[i+1] == "H" else 0)
        elif c == "Q":
            result.append("K"); i += 1
        elif c == "T":
            result.append("0" if i+1 < n and name[i+1] == "H" else "T")
            i += 1
        elif c in "VW":
            result.append("F" if c == "V" else "W")
            i += 1
        elif c == "X":
            result.append("KS"); i += 1
        elif c == "Z":
            result.append("S"); i += 1
        else:
            i += 1
    return "".join(result)

def test():
    assert soundex("Robert") == "R163"
    assert soundex("Rupert") == "R163"
    assert soundex("Ashcraft") == "A261"
    assert soundex("") == ""
    m1 = metaphone("Smith")
    m2 = metaphone("Schmidt")
    assert len(m1) > 0 and len(m2) > 0
    print("  soundex: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else:
        name = sys.argv[2] if len(sys.argv) > 2 else "Robert"
        print(f"Soundex({name}): {soundex(name)}")
