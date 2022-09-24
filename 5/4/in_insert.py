def my_insert(l, v):
    assert type(v) == int
    assert type(l) == list
    i = bin(l, v)
    l[i:i] = [v]

def bin(s, v):
    l = 0
    h = len(s)
    while l < h:
        m = (l + h) // 2
        if   s[m] == v: return m
        elif s[m] <  v: l = m + 1
        else          : h = m - 1
    return l # == h