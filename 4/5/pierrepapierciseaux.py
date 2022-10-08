from random import seed, randint

def bat(j1, j2): # 0 : PIERRE, 1 : FEUILLE, 2 : CISEAUX
    return j1 == (j2 + 2) % 3

def symbol(s):
    if s == 0: return "Pierre"
    if s == 1: return "Feuille"
    if s == 2: return "Ciseaux"

def status(s):
    if s ==  1: return "est battu par"
    if s ==  0: return "annule"
    if s == -1: return "bat"

def match(j1, j2):
    if bat(j1, j2):
        return 1
    elif j1 == j2:
        return 0
    else:
        return -1

seed(int(input()))
points = 0
for i in range(0, 5):
    j1 = randint(0, 2)
    j2 = int(input())
    point = match(j1, j2)
    points += point
    print(f"{symbol(j1)} {status(point)} {symbol(j2)} : {points}")

if 0 < points:
    print("Gagné")
elif points == 0:
    print("Nul")
else:
    print("Perdu")