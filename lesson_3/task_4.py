"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

x = []
for i in range(30):
    x.append(random.randint(1, 100))
print(x)

coun = 0
number = 0

for i in x:
    if x.count(i) > coun:
        coun = x.count(i)
        number = i
print(f'Число {number} встречается {coun} раз')