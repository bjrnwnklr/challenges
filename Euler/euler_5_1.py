# find all prime numbers up to the target number:
from time import thread_time

target = 20

factors = set()

sieve = [x for x in range(2, target + 1)]

for i in sieve:
    to_try = [x for x in sieve if i*i <= x]
    for t in to_try:
        if t % i == 0:
            sieve.remove(t)


print('Prime numbers up to %d:' % target)
print(sieve)

# find prime factors 
import math

# find the largest k so that x ** k < target e.g. 4 for 2**4 = 16 < 20
factors = {x ** math.floor(math.log(target, x)) for x in sieve}

print(sorted(factors))
result = 1
for n in factors:
    result *= n

print('Result = %d' % result)
print(thread_time())