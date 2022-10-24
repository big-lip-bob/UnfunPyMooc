def intersection(a, b): # https://en.wikipedia.org/wiki/Longest_common_substring_problem # flemme
    if len(b) < len(a): a, b = b, a
    i = 0
    for k in range(len(a), 0, -1):
        for n in range(i+1):
            if v[n:k+n] in w:
                return v[n:k+n]
        i += 1
    return ''
