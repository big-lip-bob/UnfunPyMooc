epsilon = 10 ** -6
def absdiff(a, b):
    if a < b: return b - a
    else: return a - b

init = float(input())

lastFact = 1 * 1
lastPow  = 1 * init

aprox = 0
preva = -init

count = 1
while True:

    aprox += lastPow / lastFact * (-1, 1)[count % 2]

    if absdiff(aprox, preva) < epsilon: break

    lastPow  *= init * init
    lastFact *= (count * 2) * (count * 2 + 1)

    preva = aprox
    count += 1

print(aprox)