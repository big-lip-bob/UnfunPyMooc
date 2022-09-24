def acrostiche(txt):
    s = ""
    with open(txt, encoding="UTF8") as file:
        for line in file: s += line[0]
    return s