import math


x = float(input('Enter x: '))

sum = 0

for n in range(0, 170):
    sum += (math.pow(-1, n) * math.pow(x, 2 * n + 1)) / ((2 * n + 1) * math.factorial(n))

result = 2 / math.sqrt(math.pi) * sum

print(f'erf({x}) = {result}')
