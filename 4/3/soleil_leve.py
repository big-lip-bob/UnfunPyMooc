def soleil_leve(lever, coucher, heure):
    if lever == coucher == 0: return True
    if lever == coucher == 12: return False
    if lever <= coucher: return lever <= heure < coucher
    return lever <= heure or heure < coucher
