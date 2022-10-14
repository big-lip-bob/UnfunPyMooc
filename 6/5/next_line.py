def next_line(l):
    if not l: return [1]

    i = 0
    o = []
    while i < len(l):
        n = l[i]
        c = 1
        while i + c < len(l) and n == l[i + c]: c += 1
        o.extend((c, n))
        i += c

    return o