# Целочисленный список размера N. Увеличить все нечетные числа на исходное значение последнего нечетного числа.
# Если нечетных чисел нет оставить без изменения.

import random


size = input('Введите размер массива:\n')
while type(size) != int:
    try:
        size = int(size)
    except ValueError:
        print('Ввели неверно!!!')
        size = input('Введите размер массива:\n')
abc = []
count = 0
while count < size:
    abc.append(random.randint(-100, 100))
    if abc[count] % 2 == 1:
        digit = abc[count]
    count += 1
print('Исходный массив:\n')
print(abc)
print('Последнее четное число:', digit, '\n')
for x in range(len(abc)):
    if abc[x] % 2 == 1:
        abc[x] += digit
print('Измененный массив:\n')
print(abc)

