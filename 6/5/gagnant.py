def rotate(x, y): return y, -x
def flip  (x, y): return -x, -y

directions = [(1, i) for i in range(2)]

width, height = 7, 6
def bounds(x, y): return 0 <= y < height and 0 <= x < width

win = 4
def check(x, y, g):
    player = g[y][x]
    for dir in directions:
        for dir in [dir, rotate(*dir)]:
            seq = 1
            for dir in [dir, flip(*dir)]:
                nx, ny = x + dir[0], y + dir[1]
                while bounds(nx, ny) and g[ny][nx] == player:
                    seq += 1
                    nx, ny = nx + dir[0], ny + dir[1]
                    if win <= seq: return player


empty = 'V'
def highest(x, g):
    for y in range(height):
        if g[y][x] == empty: return y
    return height


def gagnant(g):
    for x in range(width):
        if y := highest(x, g):
            if winner := check(x, y - 1, g): return winner