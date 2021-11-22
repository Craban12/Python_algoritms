import string

let1 = input('Введите букву 1:')
let2 = input("Введите букву 2:")

stroka5 = string.ascii_lowercase
let1 = let1.lower()
let2 = let2.lower()
indlet1 = stroka5.index(let1)
indlet2 = stroka5.index(let2)
print(f'{let1}:{indlet1+1}, {let2}:{indlet2+1}, количество букв между {let1} и {let2}:{indlet2-indlet1-1}')
