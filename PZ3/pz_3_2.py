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

sum = a + b + c
lar1 = max(a, b, c)
lar2 = sum - lar1 - min(a, b, c)
print("Сумма двух наибольших чисел равна:", lar1 + lar2)








