# Calculate prime numbers and their factors - efficient algorithm
# then calculate the sum of the divisors using the prime factors and powers
# then calculate "buddies" so that 


from collections import defaultdict

def buddy(start, limit):
    result = 'Nothing'
    for n in range(start, limit + 1):
        m = s_prop_divs(n) - 1
        if m > n and s_prop_divs(m) == n + 1:
            result = [n, m]
            break
    return result
    
# calculate sum of proper divisors
# uses the prime factors and their powers
# sum of prime factors s_of_d =
#   (p1^0 + p1^1 + p1^n...) * (p2^0 + p2^1 + ...)
def s_prop_divs(n):
    factors, powers = prime_powers(n)
    s_of_d = 1
    for f in factors:
        s_of_d *= sum(f ** i for i in range(powers[f] + 1))
    return s_of_d - n
    
# calculate prime factors f and their powers p for n
# so that f1^p1 * f2^p2 * ... = n
# return set of prime factors and dict with respective powers
def prime_powers(n):
    target = n
    factors = set()
    powers = defaultdict(int)

    i = 2
    while i*i <= target:
        if target % i:
            i += 1
        else:
            powers[i] += 1
            factors.add(i)
            target = target // i

    if target > 1:
        powers[target] += 1
        factors.add(target)

    return factors, powers
