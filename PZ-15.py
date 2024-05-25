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

#Функция для поиска клиента по коду помещения
def find_client_by_code(code):
    cursor.execute("SELECT * FROM CLIENT WHERE code=?", (code,))
    return cursor.fetchall()

#Функция для поиска клиента по стоимости аренды
def find_client_by_rental_cost(rental_cost):
    cursor.execute("SELECT * FROM CLIENT WHERE rental_cost=?", (rental_cost,))
    return cursor.fetchall()

# для удаления клиента по ФИО
def delete_client_by_fio(fio):
    cursor.execute("DELETE FROM CLIENT WHERE FIO=?", (fio,))
conn.commit()

#Функция для удаления клиента по коду помещения
def delete_client_by_code(code):
    cursor.execute("DELETE FROM CLIENT WHERE code=?", (code,))
conn.commit()

#Функция для удаления клиента по стоимости аренды
def delete_client_by_rental_cost(rental_cost):
    cursor.execute("DELETE FROM CLIENT WHERE rental_cost=?", (rental_cost,))
conn.commit()

#Примеры использования функций
add_client("Иванов Иван Иванович", 101, 12, 12000.00)
add_client("Петров Петр Петрович", 102, 6, 6000.00)
add_client('Алексеенко Анндрей Приветович', 105, 7, 15000.00)

print(find_client_by_fio("Иванов Иван Иванович"))
print(find_client_by_fio("Петров Петр Петрович"))
print(find_client_by_fio("Алексеенко Анндрей Приветович"))

print(find_client_by_code(102))
print(delete_client_by_rental_cost(6000.00))

delete_client_by_fio("Иванов Иван Иванович")
