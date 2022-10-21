from random import randint, seed
def alea_dice(rnd): return seed(rnd) or {randint(1, 6) for i in range(0, 3)} == {1, 2, 4}