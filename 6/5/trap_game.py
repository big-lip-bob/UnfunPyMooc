from random import randint

GOLD, TRAP = 1, -1

def create_map(size, traps):
    if size < 1 or size * size - 1 < traps: raise "Invalid arguments"
    def r(): return (randint(1, size), randint(1, size))

    map = { r(): GOLD }
    while len(map) <= traps:
        if (pos := r()) not in map: map[pos] = TRAP
    return map

def play_game(size, map):
    def bounds(*l): return all(1 <= n <= size for n in l)
    while True:
        while not bounds(*(pos := tuple(int(n) for n in input().split(' ')))): print("Entrez une valeur valide")
        if pos in map: return map[pos] == GOLD
