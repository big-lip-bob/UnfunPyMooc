def symetrie_horizontale(m):
    for y in range(0, len(m)):
        for x in range(0, len(m) // 2):
            m[x][y], m[-1-x][y] = m[-1-x][y], m[x][y]
    return m