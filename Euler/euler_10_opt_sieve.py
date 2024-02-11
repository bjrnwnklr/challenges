'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


Optimized Sieve of Eratosthenes:
- get rid of all even numbers so only odd numbers get sieved
- odd numbers: 2*i + 1
- as seen in https://projecteuler.net/overview=010
'''

import math

target = int(2e6)
sievebound = target // 2
sieve = [False for _ in range(sievebound + 1)]
crosslimit = (int(math.sqrt(target)) - 1) // 2
# False = number not crossed out yet

# sieve of eratosthenes, using a list of boolean values
# index of list is the actual numbers to be tested
for i in range(1, crosslimit + 1): 
    if not sieve[i]:
        for j in range(2 * i * (i + 1), sievebound + 1, 2 * i + 1):
            sieve[j] = True

primes = [2] + [2 * (x) + 1 for x in range(1, len(sieve)) if not sieve[x]]
print(sum(primes))