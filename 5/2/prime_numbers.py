def prime_numbers(n):
    if type(n) != int or n < 0: return None
    primes = [2, 3, 5, 7, 11, 13]
    if n < len(primes): return primes[:n]
    maybe = 17
    while len(primes) < n:
        for div in primes:
            if maybe % div == 0: break
        else: primes.append(maybe)
        maybe += 2
    return primes