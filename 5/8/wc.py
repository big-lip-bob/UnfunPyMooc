import re # regex yikes

def wc(txt):
    char = 0
    word = 0
    line = 0
    with open(txt, encoding="UTF8") as file:
        for enil in file:
            char += len(enil)
            word += len([c for c in re.split("\\W+", enil) if c != ''])
            line += 1
    return (char, word, line)