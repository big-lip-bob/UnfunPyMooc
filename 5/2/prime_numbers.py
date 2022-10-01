def prime_numbers(n):
    if type(n) != int or n < 0: return None
    primes = [2, 3] # 3, 5, 7, 11, 13]
    if n < len(primes): return primes[:n]

    maybe = 5
    sqrt = maybe ** 0.5

    while len(primes) < n:
        idx = 1
        while primes[idx] <= sqrt:
            if maybe % primes[idx] == 0: break
            idx += 1
        else: primes.append(maybe)
        maybe += 2
        sqrt = maybe ** 0.5
    return primes