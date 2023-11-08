#Даны три числа, найти сумму двух наибольших из них.
def summ():
    a =int(input('Введите первое число:\n'))
    b =int(input('Введите второе число:\n'))
    c =int(input('Введите третье число:\n'))
    list1 = [a,b,c]
    list1.sort()
    list1.reverse()
    return list1[:-1]

f = summ()
k = sum(f)
print('Сумма двух наибольших введенных чисел равна:', k)
