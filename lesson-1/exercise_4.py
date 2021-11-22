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
