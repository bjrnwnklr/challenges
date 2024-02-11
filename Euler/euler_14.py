'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

# this solution uses a generator to generate the next collatz number:
# it's a bit overkill as just counting the number of numbers would be enough...

def collatz(n):
    while n > 1:
        if n % 2 != 0:
            x = 3 * n + 1
        else:
            x = n // 2
        yield x
        n = x
    return n

results = dict()

# generate collatz numbers up to a million and store the length in a dict
for i in range(1000000):
    results[i] = len([x for x in collatz(i)])

# get maximum out of dict
m = max(results, key = results.get)
print('Longest chain for %d: %d' % (m, results[m]))


