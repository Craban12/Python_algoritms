"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

def sorter(numbers):
    i = 0
    for num in str(numbers):
        i += int(num)
    return i

data = input('Введите числа:')
das = data.split(' ')
das.sort(key=sorter, reverse=True)
print(f'Максимальное число из списка чисел:{das[0]}. Его сумма = {sorter(das[0])}')
