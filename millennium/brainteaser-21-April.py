"""
Functions f(n) and g(n) are defined below as

n(4n-1)(4n-2)(f(n)-f(n-1)) = 1, f(1) = 1/6
n(4n+1)(4n+2)(g(n)-g(n-1)) = 1, g(1) = 1/30

By writing code or otherwise compute

F = f(2024) and G = g(2024)

What is F + 3 - G?

Result: PI (3.141592653586027)
"""
f_dict = {1: 1/6}
g_dict = {1: 1/30}

def f(n):
    m = 1
    result = 1/6
    while m < n:
        m += 1
        result += 1/(m * (4*m - 1) * (4*m - 2))
    return result

def g(n):
    m = 1
    result = 1/30
    while m < n:
        m += 1
        result += 1/(m * (4*m + 1) * (4*m + 2))
    return result

def main():
    F = f(2024)
    G = g(2024)
    print(F)
    print(G)
    print(F + 3 - G)

if __name__ == '__main__':
    main()