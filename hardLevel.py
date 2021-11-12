import math


if __name__ == '__main__':
    x = float(input('Enter x: '))

    for n in range(0, 170):
        sum += (math.pow(-1, n) * math.pow(x, 2 * n + 1)) / ((2 * n + 1) * (math.sqrt(2 * math.pi * n)
                                                                            * math.pow(n, n)
                                                                            * math.pow(math.e, n * (-1))))

    result = 2 / math.sqrt(math.pi) * sum

    print(f'erf({x}) = {result}')
