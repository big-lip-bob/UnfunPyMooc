import math

seeds, area_per_seed = 1000, 50
def bonne_planete(diametre): return seeds * area_per_seed <= math.pi * diametre * diametre

print("Bonne planète" if bonne_planete(int(input())) else "Trop petite")