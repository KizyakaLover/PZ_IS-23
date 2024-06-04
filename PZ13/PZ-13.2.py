# в матрице элементы второго столбца заменяются элементами из одномерного динамического массива соответствующего размера

import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]


array = [random.randint(1, 10) for _ in range(5)]

print("Исходная матрица:")
for x in matrix:
    print(x)

print("\nОдномерный массив:")
print(array)

matrix1 = [row[:1] + [array[i]] + row[2:] for i, row in enumerate(matrix)]

print("\nМатрица с замененными элементами второго столбца:")
for x in matrix1:
    print(x)
