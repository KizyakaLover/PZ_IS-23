# -*- coding: utf-8 -*-
with open("text18-31.txt", "r", encoding='utf-8') as file1:
    content = file1.read()
    letter_count = sum(c.isalpha() for c in content)

    print("Содержимое файла:")
    print(content)
    print("Количество символов, принадлежащих к группе букв:", letter_count)


min_line = min(content.splitlines(), key=len)


with open("short.txt", "w", encoding='utf-8') as file2:
    file2.write(min_line)


