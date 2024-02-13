with open("positive_numbers.txt", "w", encoding="utf-8") as file1:
    numbers1 = [2, 5, 8, 10, 15]
    for num in numbers1:
        file1.write(str(num) + "\n")

with open("negative_numbers.txt", "w", encoding="utf-8") as file2:
    numbers2 = [-3, -7, -12, -18, -25]
    for num in numbers2:
        file2.write(str(num) + "\n")

# Чтение чисел из файлов и запись результатов в новый файл в формате UTF-8
with open("positive_numbers.txt", "r", encoding="utf-8") as file1, open("negative_numbers.txt", "r", encoding="utf-8") as file2, open("resulte.txt", "w", encoding="utf-8") as file3:
    nums1 = [int(num.strip()) for num in file1.readlines()]
    nums2 = [int(num.strip()) for num in file2.readlines()]

    elements = nums1 + nums2
    num_elements1 = len(nums1)
    num_elements2 = len(nums2)

    elements_first_third = elements[:int(len(elements)/3)]
    min_element_first_third = min(elements_first_third)

    file3.write("Элементы первого файла: {}\n".format(nums1))
    file3.write("Элементы второго файла: {}\n".format(nums2))
    file3.write("Количество элементов первого файла: {}\n".format(num_elements1))
    file3.write("Количество элементов второго файла: {}\n".format(num_elements2))
    file3.write("Элементы первой трети: {}\n".format(elements_first_third))
    file3.write("Минимальный элемент первой трети: {}\n".format(min_element_first_third))

