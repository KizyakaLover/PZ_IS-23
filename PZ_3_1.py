def check():
    triangle = [a, b, c]
    if a == b or b == c or a == c:
        return('Треугольник a,b,c - равнобедренный')
    else:
        return('Треугольник a,b,c - неравнобедренный')


a =int(input('Введите первое число:\n'))
b =int(input('Введите второе число:\n'))
c =int(input('Введите третье число:\n'))
result = check()
print(result)