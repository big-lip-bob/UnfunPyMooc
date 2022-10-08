def soleil_leve(lever, coucher, heure):
    return (((lever <= heure) + (heure < coucher)) // ((lever < coucher) + 1) > 0, not lever)[lever == coucher]