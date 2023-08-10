"""
def strcount(s):  #N**2
    for sym in set(s):
        counter = 0
        for sab_sym in s:
            if sym == sab_sym:
                counter += 1
        print(sym, counter)

strcount('aabdssra')
"""

def strcount(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    for sym, count in syms_counter.items():
        print(sym, count)

strcount('adfjfnrfjnrnurrbha')

#hefhebuihwiuhf
