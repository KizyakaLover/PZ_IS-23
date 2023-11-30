# Дан список размера N все элементы которого кроме последнего упорядочены по возрастанию.
# Сделать список упорядоченным переместив последний элемент на новую позицию
import random
size = int(input('Введите длинну массива:\n'))
zxc = []
i = 0
while i < size:
    zxc.append(random.randint(0,100))
    i += 1
zxc.sort()
zxc.append(random.randint(0,100))
print('Исходный массив:\n', zxc)
print('Упорядоченный массив:\n', sorted(zxc))
