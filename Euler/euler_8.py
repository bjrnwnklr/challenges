'''
The four adjacent digits in the 1000-digit number that have the greatest product
 are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that
 have the greatest product. What is the value of this product?
'''

f = ''.join(open(r'8_input.txt').read().split())


r = 13

results = dict()

for i in range(len(f)-r):
    prod = 1
    to_test = f[i:i+r]
    if not '0' in to_test:
        for j in f[i:i+r]:
            prod *= int(j)
        results[i] = prod

max_prod = max(results, key = results.get)
print(max_prod, list(f[max_prod:max_prod+r]), results[max_prod])