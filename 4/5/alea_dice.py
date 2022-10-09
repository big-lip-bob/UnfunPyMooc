from random import randint, seed

def alea_dice(rnd):
    seed(rnd)
    throws = [0] * 6
    for i in range(0, 3): throws[randint(1, 6) - 1] += 1
    return throws == [1, 1, 0, 1, 0, 0]