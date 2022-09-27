epsilon = 10 ** -6
init = float(input())
aprox = 0

lastFact = 1 * 1
lastPow  = 1 * init

count = 1
while True:

    term = lastPow / lastFact
    aprox += term * (-1, 1)[count % 2]

    if abs(term) < epsilon: break

    lastPow  *= init * init
    lastFact *= (count * 2) * (count * 2 + 1)

    count += 1

print(aprox)