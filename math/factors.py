from functools import reduce

# Returns list of factors of n sorted from smallest to largest.
def factors(n):    
    return sorted(list(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

# Returns list of prime factors of n. They are automatically sorted by the algorithm's logic.
def pFactors(n):
    p = []
    i = 2
    while n != 1:
        while n % i == 0:
            n /= i
            p.append(i)
        i += 1
    return p
