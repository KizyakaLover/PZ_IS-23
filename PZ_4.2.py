# Дано целое число N (> 0). С помощью операций деления нацело и взятия остатка от деления определить, имеются ли в записи числа N нечетные цифры. Если имеются, то вывести True, если нет — вывести False.
N = input('Введите число:\n')

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input('Введите число:\n')
result = False

while N > 0:
    step1 = N % 10
    if step1 % 2 != 0:
        result = True
        break
    N //= 10

print(result)