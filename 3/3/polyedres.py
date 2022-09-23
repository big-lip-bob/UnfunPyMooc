import math

poly = input()
cube = math.pow(float(input()), 3)

sqrt2d3 = math.sqrt(2) / 3

if   poly == "T": print(cube * sqrt2d3 / 4)
elif poly == "C": print(cube)
elif poly == "O": print(cube * sqrt2d3)
elif poly == "D": print(cube * (15 + 7 * math.sqrt(5)) / 4)
elif poly == "I": print(cube *  5 * (3 + math.sqrt(5)) / 12)
else: print("Polyèdre non connu")