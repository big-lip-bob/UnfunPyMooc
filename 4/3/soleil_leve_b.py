def soleil_leve(lever, coucher, heure):
    if lever == coucher == 0: return True
    if lever == coucher == 12: return False
    if lever <= coucher: return lever <= heure < coucher
    return heure < coucher or lever <= heure

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(0, 24):
    print(f"{i}{'' if soleil_leve(a, b, i) or soleil_leve(c, d, i) else ' *'}")