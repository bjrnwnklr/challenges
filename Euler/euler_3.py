# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

#############
# this one works, but runs forever. The optimization with the sieve adds too much
# overhead that it runs really slow for large numbers


target = 13195301

sieve = [x for x in range(2, target // 2)]
factors = set()

while sieve:
    n = sieve.pop(0)
    if not target % n:
        factors.add(n)
        target = target // n
        print('Found: %d' % n)
    sieve = [x for x in sieve if x < target + 1 and x % n]

print('Factors:')
print(sorted(factors))