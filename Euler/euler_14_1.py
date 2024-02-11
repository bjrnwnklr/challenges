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

# this uses an optimized approach and only counts the numbers

collatz_len = dict()

def count_collatz(n):
    if n in collatz_len:
        return collatz_len[n]

    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + count_collatz(n // 2)
    else:
        return 2 + count_collatz((3 * n + 1) // 2)

for i in range(1, int(1e6)):
    collatz_len[i] = count_collatz(i)

m = max(collatz_len, key = collatz_len.get)
print('Longest chain for %d: %d' % (m, collatz_len[m]))