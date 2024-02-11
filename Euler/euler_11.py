# what is the greatest product of four adjacent numbers 
# in the same direction (up, down, left, right or diagonally)?

from collections import defaultdict

grid = defaultdict(lambda: 0)

for r, l in enumerate(open('11_input.txt')):
    for c, x in enumerate(l.strip().split()):
        grid[(r, c)] = int(x)

def prod_hor(r, c):
    prod = 1
    coords = [(r, c+i) for i in range(4)]
    for g in coords: 
        prod *= grid[g]
    return prod

def prod_ver(r, c):
    prod = 1
    coords = [(r+i, c) for i in range(4)]
    for g in coords: 
        prod *= grid[g]
    return prod

def prod_dia(r, c):
    prod = 1
    coords = [(r+i, c+i) for i in range(4)]
    for g in coords: 
        prod *= grid[g]
    return prod


def prod_dia_r(r, c):
    prod = 1
    coords = [(r+i, c-i) for i in range(4)]
    for g in coords: 
        prod *= grid[g]
    return prod

results = []
for r in range(20):
    for c in range(20):
        results.append(prod_hor(r, c))
        results.append(prod_ver(r, c))
        results.append(prod_dia(r, c))
        results.append(prod_dia_r(r, c))
        
print(max(results))