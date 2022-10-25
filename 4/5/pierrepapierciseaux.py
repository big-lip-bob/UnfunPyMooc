from random import seed, randint

def symbol(s): return ("Pierre", "Feuille", "Ciseaux")[s]
def bat(j1, j2): return j1 == (j2 + 2) % 3
def status(s): return ("bat", "annule", "est battu par")[s + 1]
def match(j1, j2): return bat(j1, j2) * 1 or (j1 == j2) - 1

seed(int(input()))
points = 0
for i in range(0, 5):
    [j1, j2] = [randint(0, 2), int(input())]
    point = match(j1, j2)
    points += point
    print(f"{symbol(j1)} {status(point)} {symbol(j2)} : {points}")

print("Gagné" if points > 0 else "Nul" if not points else "Perdu")