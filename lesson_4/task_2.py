"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
"""

import cProfile

def sieve1(n):
    row = set(range(2, n+1))
    while row:
        prime = min(row)
        #print(prime, end = "\t")
        row -= set(range(prime, n+1, prime))


def sieve2(n):
    a = []
    for i in range(n + 1):
        a.append(i)

    a[1] = 0

    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    #print(a)


cProfile.run('sieve1(10000)')
cProfile.run('sieve2(10000)')