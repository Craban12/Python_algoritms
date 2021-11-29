"""
 Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
 Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
 В конце следует вывести полученную матрицу.
"""

line =5        #int(input('Введите количество строк:'))
column =4      #int(input('Введите количество столбцов:'))

matrix = []

for i in range(line):
    matline = []
    for x in range(column-1):
        #matline.append(x+1)
        matline.append(int(input("Введите число:")))
    matline.append(sum(matline))
    matrix.append(matline)

for x in matrix:
    print(x)
