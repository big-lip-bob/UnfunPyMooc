facts = [1, 1, 2]
def fact(n):
    for i in range(len(facts), n + 1):
        facts.append(facts[i - 1] * i)
    return facts[n]

def div10(n):
    acc = 1
    for i in range(0, n): acc /= 10
    return acc

def absdiff(a, b):
    if a < b: return b - a
    else: return a - b

epsilon = div10(6)

count = 3

init = float(input())

initpows = [1.]
def initpow(n):
    for i in range(len(initpows), n + 1):
        initpows.append(initpows[i - 1] * init)
    return initpows[n]

aprox = init
preva = init + epsilon * 2

while absdiff(aprox, preva) > epsilon:
    preva = aprox
    term = initpow(count) / fact(count)
    if count // 2 % 2 != 0: term = -term
    aprox += term
    count += 2

print(aprox)