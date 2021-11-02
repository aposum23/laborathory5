month = input('Enter number of month: ')

if month > '6':
    print('Second part of year')
else:
    print('First part of year')

if month == '2':
    print('28 days in this month')
elif int(month) % 2 == 0:
    print('31 days in this month')
else:
    print('30 days in this month')
