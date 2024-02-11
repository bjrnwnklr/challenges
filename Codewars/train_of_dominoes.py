from collections import deque

class Dominoe():
    l = 0
    r = 0

    def __init__(self, l, r):
        self.l = l
        self.r = r

    def turn(self):
        self.l, self.r = self.r, self.l

    def matches(self, n):
        if n == self.r:
            self.turn()
            return True
        elif n == self.l:
            return True
        else: return False

    def __str__(self):
        return '[%d, %d]' % (self.l, self.r)

    def pips(self):
        return (self.l, self.r)
    

def create_set(n):
    d_set = []
    used = dict()
    for i in range(n+1):
        for j in range(i, n+1):
            x = Dominoe(i, j)
            d_set.append(x)
            used[x] = False
            if i != j:
                x = Dominoe(j, i)
                d_set.append(x)
                used[x] = False

    return d_set, used

def domino_train(n):
    d_set, used = create_set(n)

    start = d_set[1]
    used[start] = True
    stack = deque([(start, None)])
    while stack:
        dom, parent = stack.pop()
        

    return []
