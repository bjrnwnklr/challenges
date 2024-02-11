def sum_of_squares(n):
    return sum(pow(x, 2) for x in range(1, n+1))

def square_of_sum(n):
    return pow(sum(x for x in range(1, n+1)), 2)

x = 100
soq = sum_of_squares(x)
qos = square_of_sum(x)

print(soq, qos, qos-soq)