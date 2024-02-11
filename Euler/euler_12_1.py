'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

###### prime factors should help.
# if you know the prime factors and their exponents, the number
# of divisors is the product of all (exponent + 1)

from collections import defaultdict

def prime_factors(n):
    factors = defaultdict(lambda: 0)
    i = 2

    while i*i <= n:
        if n % i:
            i += 1
        else:
            factors[i] += 1
            n = n // i

    if n > 1:
        factors[n] += 1
    return factors

def num_divisors(n):
    factors = prime_factors(n)
    prod = 1
    for x in factors.values():
        prod *= (x + 1)
    return prod

# triangular numbers are calculated:
# T(n) = (n * (n + 1)) / 2

def triangular(n):
    return (n * (n + 1)) // 2


n = 1
m = 0
while True:
    x = triangular(n)
    z = num_divisors(x)
    if m < z:
        m = z
        print(m, n, x)
    #print('n = %d, T(n) = %d, factors = %d' % (n, x, len(factors(x))))
    n += 1
