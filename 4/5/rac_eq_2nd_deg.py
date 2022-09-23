import math


def rac_eq_2nd_deg(a, b, c):
    delta = b * b - 4 * a * c
    if 0 < delta:
        delta = math.sqrt(delta) / (2 * a)
        r1, r2 = -b / (2 * a) - delta, -b / (2 * a) + delta
        return (min(r1, r2), max(r1, r2))
    elif delta == 0:
        return (-b / (2 * a),)
    else: return tuple()