#!/usr/bin/env python3
"""Soundex and Metaphone phonetic algorithms."""
import sys

def soundex(name):
    if not name: return ''
    name = name.upper()
    code = name[0]
    mapping = {'B':'1','F':'1','P':'1','V':'1','C':'2','G':'2','J':'2','K':'2','Q':'2','S':'2','X':'2','Z':'2',
               'D':'3','T':'3','L':'4','M':'5','N':'5','R':'6'}
    prev = mapping.get(name[0], '0')
    for c in name[1:]:
        digit = mapping.get(c, '0')
        if digit != '0' and digit != prev: code += digit
        if c not in 'HW': prev = digit
        if len(code) == 4: break
    return (code + '0000')[:4]

def match(name1, name2):
    return soundex(name1) == soundex(name2)

if __name__ == '__main__':
    if len(sys.argv) < 2: print("Usage: soundex.py <name> | soundex.py match <name1> <name2>"); sys.exit(1)
    if sys.argv[1] == 'match':
        n1, n2 = sys.argv[2], sys.argv[3]
        s1, s2 = soundex(n1), soundex(n2)
        print(f"{n1} ({s1}) {'==' if s1==s2 else '!='} {n2} ({s2})")
    else:
        for name in sys.argv[1:]:
            print(f"{name}: {soundex(name)}")
