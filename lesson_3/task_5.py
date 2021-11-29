"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
import random

x = []
for i in range(30):
    x.append(random.randint(-100, 100))
print(x)

maxmin = []
for z in x:
    if z<0:
        maxmin.append(z)
print(f'число {max(maxmin)}, позиция {x.index(max(maxmin))}')
