#!/usr/bin/env python3
import math


if __name__ == '__main__':
    a = int(input('Write a: '))
    x = 9999

    flag = False

    while not flag:
        try:
            flag = math.sqrt(a - x) > x - 2
        except:
            x -= 1
            continue

        if flag:
            break
        else:
            x -= 1

    print(f'x = {x}')
