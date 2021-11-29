"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import randint as ran
line =3
column =3

matrix = []

for i in range(line):
    matline = []
    for x in range(column-1):
        matline.append(ran(1, 100))
    matline.append(sum(matline))
    matrix.append(matline)

miax_col = []
for num in range(column):
    mincol = []
    for z in matrix:
        mincol.append(z[num])
    miax_col.append(min(mincol))

for x in matrix:
    print(x)

print(max(miax_col))