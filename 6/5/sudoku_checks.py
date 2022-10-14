def check_rows(g):
    for y in range(9):
        seen = set()
        for x in range(9):
            n = g[y][x]
            if n in seen: return False
            seen |= {n}
    return True

def check_cols(g):
    for x in range(9):
        seen = set()
        for y in range(9):
            n = g[y][x]
            if n in seen: return False
            seen |= {n}
    return True

def check_regions(g):
    for zx in range(3):
        for zy in range(3):
            seen = set()
            for x in range(3):
                for y in range(3):
                    n = g[zy * 3 + y][zx * 3 + x]
                    if n in seen: return False
                    seen |= {n}
    return True

def check_sudoku(g): return check_rows(g) and check_cols(g) and check_regions(g)