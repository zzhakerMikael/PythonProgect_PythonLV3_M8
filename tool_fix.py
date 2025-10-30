import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('professions.db')
cursor = conn.cursor()

# Создаем таблицу
cursor.execute('''
CREATE TABLE IF NOT EXISTS professions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profession TEXT NOT NULL
)
''')

# Функция для добавления профессии
def add_profession(profession):
    try:
        cursor.execute('INSERT INTO professions (profession) VALUES (?)', (profession,))
        conn.commit()
        print(f"Профессия '{profession}' успешно добавлена!")
    except Exception as e:
        print(f"Ошибка при добавлении профессии: {e}")

# Список профессий для добавления
professions_list = [
    "Программист",
    "Врач",
    "Учитель",
    "Инженер",
    "Дизайнер",
    "Менеджер",
    "Повар",
    "Архитектор"
]

# Заполняем базу данных
for profession in professions_list:
    add_profession(profession)

# Функция для просмотра всех профессий
def show_all_professions():
    cursor.execute('SELECT * FROM professions')
    professions = cursor.fetchall()
    print("\nСписок профессий:")
    for prof in professions:
        print(f"ID: {prof[0]} | Профессия: {prof[1]}")

# Выводим список профессий
show_all_professions()

# Закрываем соединение
conn.close()
