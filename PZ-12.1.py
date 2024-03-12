import random
N = 10
sequence = [random.randint(1, 100) for i in range(N)]
print("Исходная последовательность:", sequence)

sqrs = [x**2 for x in sequence if x % 2 == 0]
print("Новая последовательность из квадратов четных элементов:", sqrs)

sum_sqrs = sum(sqrs)
avg = sum_sqrs / len(sqrs) if len(sqrs) > 0 else 0
print("Сумма квадратов четных элементов:", sum_sqrs)
print("Среднее арифметическое квадратов четных элементов:", avg)