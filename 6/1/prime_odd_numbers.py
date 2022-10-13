def binary_seek(n, l):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = low + (high - low) // 2
        p = l[mid]
        if p == n: return mid
        elif p < n: low = mid + 1
        else: high = mid - 1
    return low # == len(l)

primes = [2, 3, 5, 7, 11, 13]
def prime_numbers_up_to(upper):

    index = binary_seek(upper, primes)
    if index < len(primes): return primes[:index]

    maybe = primes[-1] + 2
    sqrt = int(maybe ** 0.5)

    while primes[-1] < upper:
        idx = 1
        while primes[idx] <= sqrt:
            if maybe % primes[idx] == 0: break
            idx += 1
        else: primes.append(maybe)
        maybe += 2
        sqrt = int(maybe ** 0.5)

    return primes[:-1]


def prime_numbers(upper): return set(prime_numbers_up_to(upper + 1))
def even(upper): return {even * 2 for even in range(0, upper // 2 + 1)}

def prime_odd_numbers(numbers):
    limit = max(numbers)
    primes = prime_numbers(limit)
    evens = even(limit)
    return (
        {number for number in numbers if number in primes},
        {number for number in numbers if number not in evens}
    )