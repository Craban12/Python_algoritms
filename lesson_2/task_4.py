"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

data = int(input("Введите число:"))
number = 1
sum = 1
for i in range(1,data):
    number *= -0.5
    sum += number
print(number, sum)
