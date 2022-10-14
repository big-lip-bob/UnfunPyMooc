def belongs_to_file(mot, file):
    with open(file, 'r', encoding="UTF-8") as file:
        for line in file:
            if line.strip() == mot:
                return True
    return False