year = input('Введите год:')

if int(year[-2:]) == 0:
    if int(year) % 400 == 0:
        print('Високосный')
    else:
        print('Не високосный')
elif int(year) % 4 == 0:
    print('Високосный')
else:
    print('Не високосный')
