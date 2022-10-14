width, height = 7, 6

def placer_pion(c, x, g):
    for y in range(height):
        if g[y][x] == 'V':
            g[y][x] = c
            return (True, g)
    return (False, g)