s, s0 = input('Введите предложение:\n'), input('Введите предложение:\n')
while type(s) != str:
    try:
        s = str(s)
    except ValueError:
        print('Ввели неправильно!!!')
        s = input('Введите предложение еще раз:\n')
while type(s0) != str:
    try:
        s0 = str(s0)
    except ValueError:
        print('Ввели неправильно!!!')
        s0 = input('Введите предложение еще раз:\n')
count = s.count(s0)
print('Кол-во ', s0, 'в предложении', s, 'равно:', count)
