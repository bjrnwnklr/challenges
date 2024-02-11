# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

result = sum(int(l.strip()) for l in open('13_input.txt'))
res_10 = str(result)[:10]
print(res_10)