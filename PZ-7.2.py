stroke = input('Введите предложение\n')
while type(stroke) != str:
    try:
        stroke = str(stroke)
    except ValueError:
        print('Ввели неверно!!!')
        stroke = input('Введите предложение еще раз\n')
words = stroke.split(' ')
min = len(words[0])
for word in words:
    if len(word) < min:
        min = len(word)
print('Букв в самом коротком слове:', min)
