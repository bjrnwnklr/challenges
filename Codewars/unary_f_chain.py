'''
Your task is to write a higher order function for chaining together a list of unary functions. In other words, it should return a function that does a left fold on the given functions.

chained([a,b,c,d])(input)
Should yield the same result as

d(c(b(a(input))))
'''
def a(n):
    return n * 4

def b(n):
    return n ** 5

def c(n):
    return n // 3

def d(n):
    return n - n // 4

l = [a, b, c, d]

'''
def chained(functions):
    c_f = lambda f1, f2: lambda x: f2(f1(x))
    result = lambda x: x
    for f in functions:
        result = c_f(result, f)
    return result
'''

def chained(functions):
    def chain(input):
        for f in functions:
            input = f(input)
        return input
    return chain
