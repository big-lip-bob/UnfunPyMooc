saut = int(input()) # [1; 99]
cible= int(input()) # [1; 99]

size = 100
now = 0 + saut
while now != 0:
    if now == cible:
        print("Cible atteinte")
        break
    print(now)
    now = (now + saut) % size
else:
    print(0) # now == 0
    print("Pas trouvée")