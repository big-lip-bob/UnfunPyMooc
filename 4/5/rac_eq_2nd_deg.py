def rac_eq_2nd_deg(a, b, c):
    delta = b * b - 4 * a * c
    if 0 < delta:
        delta = delta ** .5 / (2 * a)
        [r1, r2] = [-b / (2 * a) - delta * sign for sign in [-1, 1]]
        return (r1, r2) if r1 < r2 else (r2,  r1)
    return delta == 0 and (-b / (2 * a),) or tuple()