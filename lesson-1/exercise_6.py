"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

import string

lett = input('Введите номер буквы:')
print(string.ascii_lowercase[int(lett) - 1])
