cache = [1]
def catalan(n):
    # catalan(n) = (2n)!/((n+1)!n!) = (2n)!/((n+1)(n!)^2)
    # catalan(n + 1) =? (2(n+1))!/((n+2)!(n+1)!) = (2n+2)(2n+1) * (2n)! / ((n+1)(n!)^2) / ((n+1)(n+2))
    # catalan(n + 1) = catalan(n) * (2n + 2) * (2n + 1) / ((n + 1)(n + 2))
    if n < 2: return 1

    for i in range(len(cache) + 1, n):
        cache.append(
            cache[i - 2]
            * (i * 2 + 1)
            * (i * 2 + 2)
            / ((i + 1) * (i + 2))
        )
        
    return int(cache[n - 2] * 2)
