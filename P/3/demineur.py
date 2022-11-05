import sys
from PyQt5 import * # God spare my soul

class Demineur:

    # Rendering constants
    textHeader = 40
    textPadding = 5
    textSize = (textHeader - 2 * textPadding) * .75 # pixel -> pt

    cellSize = 10

    def __init__(self, w, h, m):
        pass

    def play(self):
        pass


def check_input():
    if len(sys.argv) != 4:
        print("Usage: python demineur.py largeur hauteur nombreMines")
        return exit(1)

    try:
        [w, h, m] = [int(n) for n in sys.argv[1:]]
    except ValueError:
        print("largeur, hauteur et nombreMines doivent être des nombres positifs (> 1)")
        return exit(1)

    if w * h <= m:
        print("largeur * hauteur doivent excéder le nombreMines")
        return exit(1)

    return w, h, m

if __name__ == "__main__":
    Demineur(*check_input()).play()