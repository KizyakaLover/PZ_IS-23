a, b = input('Введите число которое будет возводиться в степень:\n'), input('Введите степень:\n')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input('Введите число которое будет возводиться в степень:')
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input('Введите степень:\n')

while int(b) < 0:
    print("Неправильно ввели!")
    b = input('Введите степень:\n')

m = a ** int(b)
print("Результат возведения в степень:", m)

