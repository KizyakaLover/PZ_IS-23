# сгенерировать матрицу в которой нечетные элементы заменяются на 0
import random

matrix = [[random.randint(1, 10) for i in range(5)] for j in range(5)]
print("Исходная матрица:")
for x in matrix:
    print(x)

matrix1 = [[0 if x % 2 != 0 else x for x in y] for y in matrix]

print("\nМатрица с замененными нечетными элементами:")
for x in matrix1:
    print(x)








