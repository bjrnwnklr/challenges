from decimal import Decimal
import re

def count_sixes(n):
    if n == 0:
        return 0
    else:
        # sequence number n can be calculated through a fraction:
        # numerator = 2 ** (n-1) + 2 ** (n-3) + ... + 2 for (n-i) > 1
        # denominator = 2 ** n
        # i can't prove for all numbers but it works and is simpler than
        # brute force looping to generate the numbers
        # 
        # this algorithm doesn't work as the decimal precision is not big enough
        #
        # what works:
        # a(n) = 2/3 +/- 1/3 / 2**(n-1)
        # use log10(3 * 2**(n-1)) to find number of 6s (log10 gives number of 000000s of solution number)
        s = Decimal((sum(2 ** i for i in range(n-1, 1, -2)) + 2) / 2 ** n)
        print(s)
    r = re.search(r'\.(6+)', str(s))
    if r:
        return len(r.group(1))
    else:
        return 0    

store = {0: 0, 1: 1}
for i in range(2, 1000):
    store[i] = (store[i-2] + store[i-1]) / 2


    