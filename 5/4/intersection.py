def intersection(a, b): # https://en.wikipedia.org/wiki/Longest_common_substring_problem # flemme
    if len(a) < len(b): a, b = b, a

    max = 0
    seq = ''
    for i in reversed(range(-len(b), 0)):
        s = anchorSubSeq(a[:-i], b[i:])
        if max < len(s):
            max = len(s)
            seq = s

    for i in range(1, len(a) - len(b) + 1):
        s = anchorSubSeq(a[i: i + len(b)], b)
        if max < len(s):
            max = len(s)
            seq = s

    for i in range(-len(b), 0):
        s = anchorSubSeq(a[i:], b[:-i])
        if max < len(s):
            max = len(s)
            seq = s

    return seq


def anchorSubSeq(a, b):
    # assert len(a) == len(b)
    mptr = 0
    msiz = 0

    optr = 0
    size = 0

    while optr + size < len(a):
        while a[optr: optr + size] == b[optr: optr + size]:
            size += 1
            if len(a) < optr + size: break

        size -= 1

        if msiz < size:
            msiz = size
            mptr = optr

        optr += size + 1
        size = 1

    return a[mptr: mptr + msiz]