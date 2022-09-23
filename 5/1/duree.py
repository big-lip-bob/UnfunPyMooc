def duree(a, b):
    dh = b[0] - a[0]
    dm = b[1] - a[1]
    if dm < 0: dh -= 1
    return (dh % 24, dm % 60)