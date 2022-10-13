min, cnt = 97, 26

def compteur_lettres(txt):
    letters = [0] * cnt
    for c in txt.lower():
        c = ord(c)
        if min <= c < min + cnt: letters[c - min] += 1
    return {chr(min + i): letters[i] for i in range(cnt)}