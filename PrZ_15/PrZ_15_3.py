import sqlite3
from datetime import date
with sqlite3.connect('Аптека.db') as con:
    cur = con.cursor()
    cur2 = con.cursor()

    cur.execute("SELECT имя, фамилия, должность FROM Анкеты")
    result = cur.fetchall()
    print(f"\nСписок сотрудников и их должности: {result} \n")

    cur.execute("SELECT имя, фамилия, базовая_ставка FROM Анкеты")
    result = cur.fetchall()
    print(f"Список сотрудников и их базовая ставка: {result}\n")

    cur.execute("SELECT имя, фамилия FROM Анкеты WHERE отдел == 'IT'")
    result = cur.fetchall()
    print(f"Список сотрудников работающих в отделе IT: {result}\n")

    cur.execute("SELECT имя, фамилия FROM Анкеты WHERE дата_найма > '2022-01-01'")
    result = cur.fetchall()
    print(f"Список сотрудников, принятых на работу после 1 января 2022 года: {result}\n")

    cur.execute("SELECT id, дата_начала, дата_окончания, причина, диагноз, оплачен FROM Больничные_листы WHERE id_сотрудника = 42 ")
    result = cur.fetchall()
    print(f"Список болничных листов, выписанных сотруднику с id 42: {result}\n")

    cur.execute("SELECT id, id_сотрудника, дата_начала, дата_окончания, причина, диагноз FROM Больничные_листы WHERE оплачен = True ")
    result = cur.fetchall()
    print(f"Список болничных листов, оплаченных компанией: {result}\n")

    cur.execute("SELECT DISTINCT имя, фамилия FROM Больничные_листы INNER JOIN Анкеты ON Анкеты.id = Больничные_листы.id_сотрудника WHERE дата_окончания > '2023-04-01'")
    result = cur.fetchall()
    print(f"Список сотрудников, имеющих больничные на текущий месяц: {result}\n")

    cur.execute("SELECT round(avg(базовая_ставка), 1) FROM Анкеты ")
    result = cur.fetchall()
    print(f"Средняя ставка среди сотрудников: {result}\n")

    cur.execute("SELECT имя, фамилия FROM Анкеты WHERE базовая_ставка > 100000.00")
    result = cur.fetchall()
    print(f"\nСписок сотрудников, имеющих базовую ставку больше 100000: {result} \n")

    cur.execute("SELECT дата_начала, дата_окончания FROM Больничные_листы")
    first = cur.fetchall()
    print(first)
    #for i in first:
        