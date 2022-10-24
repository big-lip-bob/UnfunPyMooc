def my_insert(l, v):
    if type(v) != int: return None
    n = []
    for i in l:
        if i < v: n += [i]
        else:
            n += [v, i]
            break
    else: n += [v]
    for i in l[len(n)-1:]: n += [i]
    return n
