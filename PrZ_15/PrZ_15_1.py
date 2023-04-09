import sqlite3

connect = sqlite3.connect('Анкета.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Анкета(
    id INTEGER PRIMARY KEY,
    имя VARCHAR,
    фамилия VARCHAR,
    дата_рождения DATE,
    пол VARCHAR,
    дата_найма DATE,
    должность VARCHAR,
    отдел VARCHAR,
    базовая_ставка DECIMAL
    )
    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS Больничные_листы(
    id INTEGER PRIMARY KEY,
    id_сотрудника INTEGER,
    дата_начала DATE,
    дата_окончания DATE,
    причина VARCHAR,
    диагноз VARCHAR,
    оплачен BOOLEAN,
    FOREIGN KEY(id_сотрудника) references Анкета(id_сотрудника)
    )
    """)
