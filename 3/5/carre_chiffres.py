import math

n = int(input())
sqlen = int(math.log10(n*n)) + 1
for y in range(0, n):
    for x in range(0, n):
        print(f"{((y + 1) * (x + 1)):>{sqlen}}", end = " ")
    print()