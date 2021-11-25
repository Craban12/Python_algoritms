"""
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.
"""

import random
mini = 1
maxi = 100
i = 10
number = random.randint(mini, maxi)
while i > 0:
    i -= 1
    #print(number)
    user_number = int(input("Число:"))
    if number > user_number:
        print("Загаданное число больше")
    elif number < user_number:
        print("Загаданное число меньше")
    elif number == user_number:
        print("YOU WIN")
        break
    else:
        print("Error")
        break
else:
    print(f"Вы проиграли. \nЗагаданное число {number}.")