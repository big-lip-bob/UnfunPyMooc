def duree(a, b):
    [dh, dm] = [b[i] - a[i] for i in range(2)]
    if dm < 0: dh -= 1
    return (dh % 24, dm % 60)
