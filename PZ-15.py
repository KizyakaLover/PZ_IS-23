import sqlite3

#Подключение к базе данных
conn = sqlite3.connect('rental.db')
cursor = conn.cursor()

#Создание таблицы КЛИЕНТ, если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS CLIENT
                            (FIO TEXT, code INTEGER, rental_period INTEGER, rental_cost REAL)''')

#Функция для добавления записи в таблицу КЛИЕНТ
def add_client(fio, code, rental_period, rental_cost):
    cursor.execute("INSERT INTO CLIENT (FIO, code, rental_period, rental_cost) VALUES (?, ?, ?, ?)", (fio, code, rental_period, rental_cost))
conn.commit()

#Функция для поиска клиента по ФИО
def find_client_by_fio(fio):
    cursor.execute("SELECT * FROM CLIENT WHERE FIO=?", (fio,))
    return cursor.fetchall()




#Функция для удаления клиента по коду помещения
def delete_client_by_code(code):
    cursor.execute("DELETE FROM CLIENT WHERE code=?", (code,))
conn.commit()


def edit_client_info(code, new_info):
    cursor.execute("UPDATE CLIENT SET FIO=?, rental_period=?, rental_cost=? WHERE code=?",
                   (new_info[0], new_info[2], new_info[3], code))
    conn.commit()




#Примеры использования функций
add_client("Иванов Иван Иванович", 101, 12, 12000.00)
add_client("Петров Петр Петрович", 102, 6, 6000.00)
add_client('Алексеенко Анндрей Приветович', 105, 7, 15000.00)


print(find_client_by_fio("Иванов Иван Иванович"))
print(find_client_by_fio("Петров Петр Петрович"))
print(find_client_by_fio("Алексеенко Анндрей Приветович"))
print('\n')

edit_client_info(101,["Иванов Иван Иванович", 101, 16, 15000.00])
edit_client_info(102,["Петров Петр Петрович", 102, 3, 9000.00])
edit_client_info(105,['Алексеенко Анндрей Приветович', 105, 12, 25000.00])


print(find_client_by_fio("Иванов Иван Иванович"))
print(find_client_by_fio("Петров Петр Петрович"))
print(find_client_by_fio("Алексеенко Анндрей Приветович"))

print('\n')




print(delete_client_by_code(101))
print(delete_client_by_code(102))
print(delete_client_by_code(105))



conn.close()





