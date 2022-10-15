def parse_csv(iter, separator = ';'):
    headers = list(next(iter)[:-1].split(separator))
    return [line[:-1].split(separator) for line in iter], headers

def open_csv(file, separator = ';'):
    with open(file, 'r', encoding = "UTF-8") as file:
        return parse_csv(file, separator)

def indexKeyMap(l): return

def lesser(l, max):
    for i in l:
        if i and max < int(i): return False
    return True


[(fails, fnames), (counts, cnames)] = [open_csv(input()) for _ in range(2)] # [open_csv(["result-pass-fail-0.csv", "result-count-0.csv"][_]) for _ in range(2)] #

if not set(fnames) <= set(cnames): raise "Incomplete CSV"

points = [0] * len(cnames)
ftocm = { fnames[i]: i for i in range(len(fnames)) }
ftocm = [ftocm[cnames[i]] for i in range(len(cnames))]

max_fails = 10
for c in range(len(counts)):
    count = counts[c]
    fail = fails[c]
    if lesser(count, max_fails):
        for f in range(len(cnames)):
            if fail[ftocm[f]] == "VRAI": points[f] += 1

for _, name in sorted(zip(points, cnames), reverse = True): print(name)