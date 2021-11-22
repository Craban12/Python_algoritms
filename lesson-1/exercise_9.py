"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

num1 = int(input('Число 1:'))
num2 = int(input('Число 2:'))
num3 = int(input('Число 3:'))

if num2 <= num1 <= num3 or num3 <= num1 <= num2:
    print(f'Среднее число {num1}')
elif num1 <= num2 <= num3 or num3 <= num2 <= num1:
    print(f'Среднее число {num2}')
else:
    print(f'Среднее число {num3}')
