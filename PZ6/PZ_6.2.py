# целочисленный список А размера N.
# Сформировать новый список B по правилу элемент B(k) равен среднему арифметическому элементов списка А от 1 до K.
import random
import statistics
size = input('Введите размер массива:\n')
while type(size) != int:
    try:
        size = int(size)
    except ValueError:
        print('Ввели неправильно!!!\n')
        size = input('Введите размер массива:\n')
count = 0
massive, massive2 = [], []
while count < size:
    massive.append(random.randint(1,3))
    count += 1
print('Исходный массив:')
print(massive)
count = 0
i = 0
while count < size:
    digit = 0
    while i < size:
        digit += massive[i]
        i += 1
        massive2.append(digit/i)
        count += 1
        i = count
print('Новый массив:\n')
print(massive2)
