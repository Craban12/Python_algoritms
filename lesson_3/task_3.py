"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

x = []
for i in range(10):
    x.append(random.randint(1, 100))
print(x)

max_num = max(x)
min_num = min(x)
max_numi = x.index(max(x))
min_numi = x.index(min(x))
print('Максимум', max(x))
print('Минимум', min(x))
x[max_numi], x[min_numi] = x[min_numi], x[max_numi]

print(x)
