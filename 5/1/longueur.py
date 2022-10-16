def longueur(*p): # a quand l'iterateur sliding window ?
    if len(p) < 2: return 0
    origin = p[0]
    return sum(distance_points(origin, (origin := p)) for p in p[1:])

def distance_points(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    return (dx*dx+dy*dy) ** .5