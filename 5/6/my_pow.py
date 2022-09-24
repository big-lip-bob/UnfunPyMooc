def my_pow(n, f):
    if type(f) != float or type(n) != int: return None
    return [f**i for i in range(0, n)]