def my_insert(l, v):
    if type(v) != int: return None
    i = bin(l, v)
    l = l[:]
    l[i:i] = [v]
    return l

def bin(s, v):
    l = 0
    h = len(s)
    while l < h:
        m = (l + h) // 2
        if   s[m] == v: return m
        elif s[m] <  v: l = m + 1
        else          : h = m - 1
    return l # == h

