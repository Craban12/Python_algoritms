x1 = int(input('Введите координату X1:'))
y1 = int(input('Введите координату Y1:'))

x2 = int(input('Введите координату X2:'))
y2 = int(input('Введите координату Y2:'))

k = (y1-y2)/(x1-x2)
b = y2 - k * x2
print(f'Уравнение прямой: y = {k}x + {b}')
