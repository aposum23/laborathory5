for i in range(100, 999):
    number = str(i)
    if int(number) % 7 == 0 and (int(number[0]) + int(number[1]) + int(number[2])) % 7 == 0:
        print(i)
