def plus_grand_bord(str):
    for i in reversed(range(1, len(str))):
        if str[:i] == str[-i:]: return str[:i]
    else: return ''