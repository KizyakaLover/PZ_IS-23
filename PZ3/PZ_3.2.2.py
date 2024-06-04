# Даны три числа, найти сумму двух наибольших из них.
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


def two_largest(a, b, c):
    if a >= b or a >= c:
        lar1 = a
        if b >= c:
            lar2 = b
        else:
            lar2 = c
    elif b >= a or b >= c:
        lar1 = b
        if a >= c:
            lar2 = a
        else:
            lar2 = c
    else:
        lar1 = c
        if a >= b:
            lar2 = a
        else:
            lar2 = b
    return lar1, lar2


print('Сумма двух наибольших чисел равна:', sum(two_largest(a, b, c)))
