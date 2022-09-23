import math

def premier(n):
    if n < 2: return False
    if 2 < n and n % 2 == 0: return False
    for d in range(3, int(math.sqrt(n)) + 1, 2):
        if n % d == 0: return False
    return True

def iterPremiers(b):
    if b < 3: return
    print(2)
    for n in range(3, b, 2):
        if premier(n): print(n)

iterPremiers(int(input()))