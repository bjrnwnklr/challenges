def is_pal(x):
    return x == int(str(x)[::-1])

pals = set()

for x in range(1000):
    for y in range(1000):
        if is_pal(x*y):
            pals.add((x, y, x*y))

x, y, p = max(pals, key = lambda x: x[2])
print('%d * %d = %d' % (x, y, p))

