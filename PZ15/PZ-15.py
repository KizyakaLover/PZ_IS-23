import sqlite3

conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS CLIENT (
        CLIENT_ID INTEGER PRIMARY KEY,
        FULL_NAME TEXT,
        ROOM_CODE TEXT,
        LEASE_TERM INTEGER,
        TOTAL_COST REAL
    )
''')


def add_client(client_data):
    cursor.execute('''
        INSERT INTO CLIENT (FULL_NAME, ROOM_CODE, LEASE_TERM, TOTAL_COST) VALUES (?, ?, ?, ?)
    ''', client_data)
    conn.commit()

clients_data = [
    ("Иванов Иван Иванович", "10000", 12, 120000.0),
    ("Петров Петр Петрович", "15000", 24, 180000.0),
    ("Иванова Екатерина Максимовна", "12000", 15, 190000.0),
    ("Петрова Елизавета Ивановна", "15000", 12, 130000.0),
    ("Соколов Максим Генадьевич", "10000", 10, 120000.0),
    ("Васильев Николай Федорович", "17000", 16, 160000.0),
    ("Николаев Николай Сергеевич", "10000", 15, 150000.0),
    ("Петров Александр Алесандрович", "15000", 24, 180000.0),
    ("Миронов Антон Андреевич", "10000", 12, 120000.0),
    ("Петрова Дарья Алексеевна", "11000", 20, 160000.0),

]

for data in clients_data:
    add_client(data)

def show_table_info():
    cursor.execute("SELECT * FROM CLIENT")
    table_data = cursor.fetchall()
    for row in table_data:
        print(row)

print("\nИнформация о таблице:")
show_table_info()


def find_client_by_fio(full_name):
    cursor.execute('SELECT * FROM CLIENT WHERE FULL_NAME = ?', (full_name,))
    client = cursor.fetchone()
    if client:
        return client
    else:
        return None


def edit_client_by_full_name(full_name, new_data):
    cursor.execute('''
        UPDATE CLIENT 
        SET TOTAL_COST = ?, LEASE_TERM = ?, ROOM_CODE = ?
        WHERE FULL_NAME = ?
    ''', (*new_data, full_name))
    conn.commit()


def delete_client_by_full_name(full_name):
    cursor.execute('DELETE FROM CLIENT WHERE FULL_NAME = ?', (full_name,))
    conn.commit()

full_name_to_search = "Иванов Иван Иванович"
full_name_to_search1 = "Петрова Елизавета Ивановна"
full_name_to_search2 = "Васильев Николай Федорович"
print("\nПоиск клиента по Ф.И.О.:")
print(find_client_by_fio(full_name_to_search))
print(find_client_by_fio(full_name_to_search1))
print(find_client_by_fio(full_name_to_search2))

print("\nОтредактируем клиентов по фио")

edit_client_by_full_name("Иванов Иван Иванович", (150000.0, 18, "20000"))
edit_client_by_full_name("Иванова Екатерина Максимовна", (160000.0, 24, "25000"))
edit_client_by_full_name("Петров Александр Алесандрович", (130000.0, 12, "18000"))
print("\nИнформация о таблице после редактирования:\n")
show_table_info()

print("\nУдалим трех клиентов по фио")
delete_client_by_full_name("Иванов Иван Иванович")
delete_client_by_full_name("Петров Петр Петрович")
delete_client_by_full_name("Сидоров Сидор Сидорович")
print("\nИнформация о таблице после удаления:")
show_table_info()




