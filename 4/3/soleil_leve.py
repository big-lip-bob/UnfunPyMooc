def soleil_leve(lever, coucher, heure):
    return ( (lever <= heure) + (heure < coucher) >> (lever < coucher) > 0, lever == 0)[lever == coucher]