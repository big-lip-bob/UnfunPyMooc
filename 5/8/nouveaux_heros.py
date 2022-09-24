def nouveaux_heros(t1, t2):
    with open(t1, encoding="UTF8") as inp, open(t2, "w", encoding="UTF8") as out:
        for line in inp: out.write(line.replace("Paul", "Tom").replace("Pierre", "Paul").replace("Jacqueline", "Mathilde"))