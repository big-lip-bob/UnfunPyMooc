def top_3_candidats(moyennes):
    max = [(None, 0)] * 4
    for candidat in moyennes:
        max[-1] = (candidat, moyennes[candidat])
        for i in reversed(range(len(max)-1)):
            if max[i][1] < max[i+1][1]: max[i], max[i+1] = max[i+1], max[i]

    return tuple([candidat[0] for candidat in max[:-1]])
