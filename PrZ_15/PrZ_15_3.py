import sqlite3
from datetime import date
with sqlite3.connect('Аптека.db') as con:
    cur = con.cursor()


    cur.execute("SELECT имя, фамилия, должность FROM Анкеты")
    result = cur.fetchall()
    print(f"\n#1 Список сотрудников и их должности: {result} \n")

    cur.execute("SELECT имя, фамилия, базовая_ставка FROM Анкеты")
    result = cur.fetchall()
    print(f"#2 Список сотрудников и их базовая ставка: {result}\n")

    cur.execute("SELECT имя, фамилия FROM Анкеты WHERE отдел == 'IT'")
    result = cur.fetchall()
    print(f"#3 Список сотрудников работающих в отделе IT: {result}\n")

    cur.execute("SELECT имя, фамилия FROM Анкеты WHERE дата_найма > '2022-01-01'")
    result = cur.fetchall()
    print(f"#4 Список сотрудников, принятых на работу после 1 января 2022 года: {result}\n")

    cur.execute("SELECT id, дата_начала, дата_окончания, причина, диагноз, оплачен FROM Больничные_листы WHERE id_сотрудника = 42 ")
    result = cur.fetchall()
    print(f"#5 Список болничных листов, выписанных сотруднику с id 42: {result}\n")

    cur.execute("SELECT id, id_сотрудника, дата_начала, дата_окончания, причина, диагноз FROM Больничные_листы WHERE оплачен = True ")
    result = cur.fetchall()
    print(f"#6 Список болничных листов, оплаченных компанией: {result}\n")

    cur.execute("SELECT DISTINCT имя, фамилия FROM Больничные_листы INNER JOIN Анкеты ON Анкеты.id = Больничные_листы.id_сотрудника WHERE дата_окончания > '2023-04-01'")
    result = cur.fetchall()
    print(f"#7 Список сотрудников, имеющих больничные на текущий месяц: {result}\n")

    cur.execute("SELECT round(avg(базовая_ставка), 1) FROM Анкеты ")
    result = cur.fetchall()
    print(f"#8 Средняя ставка среди сотрудников: {result}\n")

    cur.execute("SELECT имя, фамилия FROM Анкеты WHERE базовая_ставка > 100000.00")
    result = cur.fetchall()
    print(f"#9 Список сотрудников, имеющих базовую ставку больше 100000: {result} \n")\
    

    cur.execute("SELECT имя, фамилия, sum(julianday(дата_окончания) - julianday(дата_начала)) FROM Анкеты INNER JOIN Больничные_листы ON Анкеты.id = Больничные_листы.id_сотрудника GROUP BY Анкеты.id")
    result = cur.fetchall()
    print(f"#10 Список всех сотрудников и общее количество дней, проведенных ими на больничном{result} \n")
    

    cur.execute("SELECT имя, фамилия, дата_рождения, пол, дата_найма, должность, отдел, базовая_ставка, дата_начала, дата_окончания, причина, диагноз, оплачен FROM Анкеты INNER JOIN Больничные_листы ON Анкеты.id = Больничные_листы.id_сотрудника WHERE дата_окончания > '2023-04-01'")
    result = cur.fetchall()
    print(f"#11 Информация о сотрудниках и их больничных листах за последний месяц: {result} \n")


    cur.execute("SELECT DISTINCT отдел, round(AVG(julianday(дата_окончания) - julianday(дата_начала)), 1) FROM Анкеты INNER JOIN Больничные_листы ON Анкеты.id = Больничные_листы.id_сотрудника GROUP BY Анкеты.id")
    result = cur.fetchall()
    print(f"#12 Средняя продолжительность больничных листов сотрудников в каждом отделе{result} \n   ")


    cur.execute("SELECT имя, фамилия, Больничные_листы.id, MAX(дата_начала), дата_окончания, причина, диагноз, оплачен FROM Анкеты INNER JOIN Больничные_листы ON Анкеты.id = Больничные_листы.id_сотрудника GROUP BY Анкеты.id ORDER BY дата_начала DESC ")
    result = cur.fetchall()
    print(f"#13 Список сотрудников и информацию о последнем больничном листе, который они оформляли{result} \n")


    cur.execute("SELECT имя, фамилия, Больничные_листы.id, min(дата_начала), дата_окончания, причина, диагноз, оплачен FROM Анкеты INNER JOIN Больничные_листы ON Анкеты.id = Больничные_листы.id_сотрудника GROUP BY Анкеты.id ORDER BY дата_начала DESC ")
    result = cur.fetchall()
    print(f"#14 Список сотрудников и информацию о первом больничном листе, который они оформляли{result} \n")


    cur.execute("SELECT имя, фамилия, sum(julianday(дата_окончания) - julianday(дата_начала)) FROM Анкеты INNER JOIN Больничные_листы ON Анкеты.id = Больничные_листы.id_сотрудника WHERE дата_начала > '2023-01-01' GROUP BY Анкеты.id")
    result = cur.fetchall()
    print(f"#15 Список сотрудников и суммарную продолжительность их больничных листов в текущем году{result}")