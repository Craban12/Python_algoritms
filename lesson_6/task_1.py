"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
"""

from memory_profiler import profile

@profile
def sieve1(n):
    row = set(range(2, n+1))
    while row:
        prime = min(row)
        #print(prime, end = "\t")
        row -= set(range(prime, n+1, prime))

@profile
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

sieve1(10000)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     3     19.0 MiB     19.0 MiB           1   @profile
     4                                         def sieve1(n):
     5     19.9 MiB      0.9 MiB           1       row = set(range(2, n+1))
     6     20.1 MiB   -568.5 MiB        1230       while row:
     7     20.1 MiB   -568.1 MiB        1229           prime = min(row)
     8                                                 #print(prime, end = "\t")
     9     20.1 MiB   -568.4 MiB        1229           row -= set(range(prime, n+1, prime))
"""

sieve2(10000)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    11     19.1 MiB     19.1 MiB           1   @profile
    12                                         def sieve2(n):
    13     19.1 MiB      0.0 MiB           1       a = []
    14     19.4 MiB      0.0 MiB       10002       for i in range(n + 1):
    15     19.4 MiB      0.4 MiB       10001           a.append(i)
    16                                         
    17     19.4 MiB      0.0 MiB           1       a[1] = 0
    18                                         
    19     19.4 MiB      0.0 MiB           1       i = 2
    20     19.4 MiB      0.0 MiB       10000       while i <= n:
    21     19.4 MiB      0.0 MiB        9999           if a[i] != 0:
    22     19.4 MiB      0.0 MiB        1229               j = i + i
    23     19.4 MiB      0.0 MiB       24300               while j <= n:
    24     19.4 MiB      0.0 MiB       23071                   a[j] = 0
    25     19.4 MiB      0.0 MiB       23071                   j = j + i
    26     19.4 MiB      0.0 MiB        9999           i += 1
    27     19.6 MiB      0.1 MiB           1       a = set(a)
    28     19.6 MiB      0.0 MiB           1       a.remove(0)
    29                                             #print(a)
"""
