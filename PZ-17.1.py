import tkinter as tk


def get_weekday():
    # Задаем дни недели
    weekdays = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

    # Получаем введенное пользователем число K
    K = int(entry.get())

    # Определяем номер дня недели для K-го дня года
    weekday_num = (K + 3) % 7  # 3 - это смещение от четверга

    # Выводим результат на экран
    result_label.config(text="{}-й день года - {}".format(K, weekdays[weekday_num]))


# Создаем графический интерфейс
root = tk.Tk()
root.title("Определение номера дня недели")

# Создаем и размещаем виджеты
label = tk.Label(root, text="Введите число от 1 до 365:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Определить день недели", command=get_weekday)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Запускаем главный цикл обработки событий
root.mainloop()
