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

"""
1233 function calls in 0.103 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.103    0.103 <string>:1(<module>)
        1    0.017    0.017    0.103    0.103 task_2.py:11(sieve1)
        1    0.000    0.000    0.103    0.103 {built-in method builtins.exec}
     1229    0.087    0.000    0.087    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         10006 function calls in 0.010 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
        1    0.008    0.008    0.010    0.010 task_2.py:19(sieve2)
        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
    10001    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
"""