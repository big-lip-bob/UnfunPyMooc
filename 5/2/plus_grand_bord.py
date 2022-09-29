def plus_grand_bord(str):
    for i in reversed(range(0, len(str))):
        if str[:i] == str[-i:]: return str[:i]
    return ''