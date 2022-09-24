def antisymetrique(m):
    for y in range(0, len(m)):
        for x in range(y, len(m)):
            if m[x][y] != -m[y][x]:
                return False
    return True