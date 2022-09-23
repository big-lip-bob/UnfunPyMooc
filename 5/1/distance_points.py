def distance_points(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    return (dx*dx+dy*dy) ** .5