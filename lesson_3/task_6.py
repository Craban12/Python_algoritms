"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

x = []
for i in range(30):
    x.append(random.randint(1, 100))
print(x)

xmin = x.index(min(x))
xmax = x.index(max(x))

print(xmin, xmax)
if xmin < xmax:
    print(sum(x[xmin + 1:xmax]))
    print(x[xmin+1:xmax])
else:
    print(sum(x[xmax + 1:xmin]))
    print(x[xmax+1:xmin])