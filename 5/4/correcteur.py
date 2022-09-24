def correcteur(m, l):
    min = 9
    idx = 0
    for i in range(0, len(l)):
        if len(l[i]) == len(m):
            dt = distance_mots(l[i], m)
            if dt < min:
                min = dt
                idx = i
    return l[idx]

def distance_mots(a, b): return sum([a[i] != b[i] for i in range(0, len(a))])