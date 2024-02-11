'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math

target = int(2e6)
sieve = [True for _ in range(0, target + 1)]
sieve[0] = False
sieve[1] = False

# sieve of eratosthenes, using a list of boolean values
# index of list is the actual numbers to be tested
for i in range(2, int(math.sqrt(target))+1):
    if sieve[i]:
        for j in range(2, (target // i) + 1):
            sieve[i*j] = False

primes = [x for x in range(2, len(sieve)) if sieve[x]]
print(sum(primes))