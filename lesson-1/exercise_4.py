"""
Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random
import string

xx = input("От:")
yy = input("До:")

if xx.isdigit() and yy.isdigit():
    ran = random.randint(int(xx),int(yy))
    print(ran)
elif xx.isalpha() and yy.isalpha():
    xx = xx.lower()
    yy = yy.lower()
    stroka = string.ascii_lowercase
    xs = stroka.index(xx)
    ys = stroka.index(yy)
    print(stroka[random.randint(xs, ys)])
else:
    print('Неправильно введенные данные')
