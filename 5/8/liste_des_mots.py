import re # regex yikes

def liste_des_mots(txt):
    with open(txt, encoding="UTF8") as file:
        return sorted({word.lower() for word in re.split("[\\d\\s\\-\"'?!:;.,*=()]+", line) for line in file } - {''})
