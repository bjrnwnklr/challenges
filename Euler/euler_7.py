# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
import math

target = 200
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
print(len(primes))

# print the 10001st prime (10000 since list starts at 0)
#print(primes[10000])

