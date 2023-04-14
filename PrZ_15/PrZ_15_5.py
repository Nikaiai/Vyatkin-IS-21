import sqlite3
with sqlite3.connect('Аптека.db') as con:
    cur = con.cursor()

    session.execute("DELETE FROM Больничные_листы INNER JOIN Анкеты ON Анкеты.id = Больничные_листы.id_сотрудника WHERE имя = 'Иван'")

    ##cur.execute("DELETE FROM Больничные_листы INNER JOIN Анкеты ON Анкеты.id = Больничные_листы.id_сотрудника WHERE фамилия = 'Петров'")

    ##cur.execute("DELETE FROM Больничные_листы INNER JOIN Анкеты ON Анкеты.id = Больничные_листы.id_сотрудника WHERE имя = 'мене'")

    ##

    ##

    ##

    #cur.execute("DELETE FROM Больничные_листы WHERE оплачен = FALSE")

    #cur.execute("DELETE FROM Больничные_листы WHERE дата_окончания < '2023-04-14'")

    #cur.execute("DELETE FROM Больничные_листы WHERE дата_начала > '2023-01-01'")

    #cur.execute("DELETE FROM Больничные_листы WHERE дата_окончания > '2023-01-01'")

    