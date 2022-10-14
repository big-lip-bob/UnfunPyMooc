def file_histogram(file):
    histogram = {}
    with open(file, 'r', encoding = "UTF-8") as file:
        for line in file:
            for c in line: histogram[c] = histogram.setdefault(c, 0) + 1
    return histogram

def words_by_length(file):
    words = {}
    with open(file, 'r', encoding = "UTF-8") as file:
        for line in file:
            word = ""
            while len(line):
                c = line[0]
                if c.isalpha():
                    word += c
                elif word:
                    words.setdefault(len(word), set()).add(word.lower() )
                    word = ""
                line = line[1:]
            if word: words.setdefault(len(word), set()).add(word.lower())

    for length in words: words[length] = list(sorted(words[length]))
    return words