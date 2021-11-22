a = input('Сторона а:')
b = input('Сторона b:')
c = input('Сторона c:')

if a+b < c and a+c < b and b+c < a:
    print('Треугольник не существует.')
elif a == b == c:
    print('Равносторонний')
elif a == b != c or a == c != b or b == c != a:
    print('Равнобедреный')
else:
    print('Данный треугольник разносторонний')
