def plus_grand_bord(str):
    max = 0
    for i in range(1, len(str)):
        if str[:i] == str[-i:]:
            max = i

    return str[:max]