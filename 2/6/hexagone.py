import math

long = float(input())

circ = math.pi * 2 / 6
for i in range(0, 6):
    print(math.cos(i * circ) * long, math.sin(i * circ) * long)