def SortInc3(A, B, C):
    while type(A) != float:
        try:
            A = float(A)
        except ValueError:
            print("Неправильно ввели!")
            A = input('Введите число A:\n')
    while type(B) != float:
        try:
            B = float(B)
        except ValueError:
            print("Неправильно ввели!")
            B = input('Введите число B:\n')
    while type(C) != float:
        try:
            C = float(C)
        except ValueError:
            print("Неправильно ввели!")
            C = input('Введите число C:\n')
    xd = [float(A), float(B), float(C)]
    xd.sort()
    return xd


for i in range(2):
    print(SortInc3(input('Введите число A:\n'), input('Введите число B:\n'),input('Введите число C:\n')))
