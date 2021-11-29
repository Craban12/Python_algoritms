"""
 В одномерном массиве целых чисел определить два наименьших элемента.
 Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random

x = []
for i in range(10):
    x.append(random.randint(-100, 100))
print(x)

min1 = min(x)
x.remove(min1)
min2 = min(x)

print(min1, min2)
