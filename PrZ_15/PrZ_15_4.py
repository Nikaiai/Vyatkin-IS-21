import sqlite3
with sqlite3.connect('Аптека.db') as con:
    cur = con.cursor()

    cur.execute("UPDATE Анкеты SET базовая_ставка = 41000.00 WHERE id = 1")
    
    cur.execute("UPDATE Анкеты SET отдел = 'PR' WHERE дата_рождения BETWEEN '1990-01-01' AND '2023-10-04' ")

    cur.execute("UPDATE Анкеты SET дата_найма = '2023-04-10' WHERE id = 1")

    #cur.execute("UPDATE Больничные_листы SET  причина = 'Болезнь' where id = 341206")

    #cur.execute("UPDATE Анкеты INNER JOIN Больничные_листы ON оплачен = True SET базовая_ставка = 150000.00 ")

    cur.execute("UPDATE Больничные_листы JOIN Анкеты ON отдел = Бухгалтерия SET причина = 156 ")