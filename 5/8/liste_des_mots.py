import re # regex yikes

def liste_des_mots(txt):
    l = set()
    with open(txt, encoding="UTF8") as inp:
        for line in inp: l |= set([c.lower() for c in re.split("[\\d\\s\\-\"'?!:;.,*=()]+", line)])
    return sorted(l - {''})