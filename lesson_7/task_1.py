"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint
def sort_bbb(N):
    ran_list = []
    for i in range(N):
        ran_list.append(randint(-100, 100))
    print(ran_list)
    for i in range(N-1):
        for j in range(N-i-1):
            if ran_list[j] < ran_list[j+1]:
                b = ran_list[j]
                ran_list[j] = ran_list[j+1]
                ran_list[j+1] = b
    print(ran_list)

sort_bbb(20)