pari = int(input()) # [0; 16]
tirage = int(input()) # [0; 12]

print(10 * (((tirage != 0) & ((tirage <= 10) ^ tirage ^ pari), (tirage ^ pari) & 1)[pari < 15] * 2, (tirage == pari) * 12)[pari < 13])

"""
if pari <= 12:# [0; 12]
    if tirage == pari: print(mise * 12)
    else: print(mise * 0)
elif pari <= 14: # [13; 14]
    if tirage % 2 != pari % 2: print(mise * 2)
    else: print(mise * 0)
else: # [15; 16]
    if tirage != 0 and ((tirage <= 10) ^ (tirage % 2 != pari % 2)): print(mise * 2)
    else: print(mise * 0)
"""