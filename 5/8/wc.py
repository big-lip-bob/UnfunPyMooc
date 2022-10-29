def wc(txt):
    char = 0
    word = 0
    line = 0
    with open(txt, encoding="UTF8") as file:
        for enil in file:
            char += len(enil)
            word += len(enil.split())
            line += 1
    return (char, word, line)
