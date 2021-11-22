#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input('Введите трехзначное число:')
x_sum = 0
if len(number) == 3 and number.isdigit():
    for x_num in number:
        x_sum += int(x_num)
    print('Сумма цифр:', x_sum)
else:
    print("Введено неверное значение!")
