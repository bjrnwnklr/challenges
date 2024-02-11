'''
seven(times(five)) # must return 35
four(plus(nine)) # must return 13
eight(minus(three)) # must return 5
six(divided_by(two)) # must return 3
'''

def zero(f=None):
    return num('0', f)
def one(f=None): 
    return num('1', f)
def two(f=None):
    return num('2', f)
def three(f=None):
    return num('3', f)
def four(f=None):
    return num('4', f)
def five(f=None):
    return num('5', f)
def six(f=None):
    return num('6', f)
def seven(f=None):
    return num('7', f)
def eight(f=None):
    return num('8', f)
def nine(f=None):
    return num('9', f)

def plus(n):
    return ops('+', n)
def minus(n):
    return ops('-', n)
def times(n):
    return ops('*', n)
def divided_by(n):
    return ops('//', n)

def ops(o, n): 
    return o + n

def num(n, f=None):
    return n if f is None else eval(n + f)

