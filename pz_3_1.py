# Даны три числа a, b, c. Проверить истинность высказывания "треугольник a, b, c - равнобедренный"
a, b, c = input('Введите первую сторону:\n'), input('Введите вторую сторону:\n'), input('Введите третью сторону:\n')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input('Введите первую сторону:\n')
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input('Введите вторую сторону:\n')
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print("Неправильно ввели!")
        c = input('Введите третью сторону:\n')


def traingle():

    if a == b or a == c or b == c:
        return 'Треугольник - равнобедренный'
    else:
        return "Треугольник - неравнобедренный"


print(traingle())
