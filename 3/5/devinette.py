import random

hidden = random.randint(0, 100)
max = 6
tries = 0
while True:
    guess = int(input())
    tries += 1
    if hidden == guess:
        print(f"Gagné en {tries} essai(s) !")
        break
    if tries < max: print("Trop grand" if hidden < guess else "Trop petit")
    else:
        print(f"Perdu ! Le secret était {hidden}")
        break