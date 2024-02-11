##########################
# THis one runs very fast and efficient

init_target = 20
target = init_target

factors = set()

i = 2

while i*i <= target:
    if target % i:
        i += 1
    else:
        factors.add(i)
        target = target // i

if target > 1:
    factors.add(target)
print(factors)
print('Sum of factors:', sum(factors) + 1 + init_target)