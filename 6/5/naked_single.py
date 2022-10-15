def cartesian(w, h):
    for y in range(h):
        for x in range(w):
            yield (x, y)

def tryCollapse(g, x, y):
    n = g[y][x]
    if type(n) == set: return 0
    changes = False
    for f in [collapseRow, collapseColumn, collapseSquare]:
        if (state := f(g, x, y ,n)):
            if state < 0: return -1
            changes = True
    return changes

def collapseAt(g, x, y, n):
    s = g[y][x]
    if type(s) == set:
        if n in s:
            s -= {n}
            if len(s) == 1: g[y][x] = next(n for n in s)
            return s and 1 or -1
    return 0

def collapseRow(g, x, y, n):
    changes = False
    for x in range(9):
        if (state := collapseAt(g, x, y ,n)):
            if state < 0: return -1
            changes = True
    return changes

def collapseColumn(g, x, y, n):
    changes = False
    for y in range(9):
        if (state := collapseAt(g, x, y ,n)):
            if state < 0: return -1
            changes = True
    return changes

def collapseSquare(g, x, y, n):
    changes = False
    xq, yq = x // 3 * 3, y - y % 3
    for y in range(3):
        for x in range(3):
            if (state := collapseAt(g, xq + x, yq + y ,n)):
                if state < 0: return -1
                changes = True
    return changes


def naked_single(sudoku):

    for (x, y) in cartesian(9, 9):
        if sudoku[y][x] == 0:
            sudoku[y][x] = set(i+1 for i in range(9))

    last_collapse = (9 - 1, 9 - 1)
    while True:
        for (x, y) in cartesian(9, 9):
            if (state := tryCollapse(sudoku, x, y)):
                if state < 0: return (False, None)
                last_collapse = (x, y)
            elif (x, y) == last_collapse:
                print(x, y)
                break
        else: continue
        break

    for (x, y) in cartesian(9, 9):
        if type(sudoku[y][x]) != int: return (False, None)
    return (True, sudoku)