import math


if __name__ == '__main__':
    x = float(input('Enter x: '))
    a = math.pow(x * (-1), 3) / 3
    sum = a
    for n in range(1, 170):
        a *= ((2 * n + 1) * math.pow(x, 2)) / ((2 * n + 3) * (n + 1))
        sum += a

    res = 2 / math.sqrt(math.pi) * sum

    print(f'erf({x}) = {res}')
