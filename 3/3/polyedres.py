poly = input()
cube = float(input()) ** 3

sqrt2d3 = 2 ** .5 / 3

if   poly == "T": print(cube * sqrt2d3 / 4)
elif poly == "C": print(cube)
elif poly == "O": print(cube * sqrt2d3)
elif poly == "D": print(cube * (15 + 7 * 5 ** .5) / 4)
elif poly == "I": print(cube *  5 * (3 + 5 ** .5) / 12)
else: print("Polyèdre non connu")