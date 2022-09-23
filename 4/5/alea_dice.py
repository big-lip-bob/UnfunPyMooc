from random import randint, seed

def alea_dice(rnd):
    seed(rnd)
    throws = [False] * 6
    for i in range(0, 3):
        throws[randint(1, 6) - 1] = True  # ^=

    return throws[1 - 1] and throws[2 - 1] and throws[4 - 1]

