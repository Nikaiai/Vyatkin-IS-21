import sqlite3
with sqlite3.connect('Аптека.db') as con:
    cur = con.cursor()
#1, 11
    #cur.execute("DELETE FROM Больничные_листы WHERE id_сотрудника = (SELECT DISTINCT id FROM Анкеты WHERE имя = 'Иван')")
#2
    #cur.execute("DELETE FROM Больничные_листы WHERE id_сотрудника = (SELECT DISTINCT id FROM Анкеты WHERE фамилия = 'Петров')")
#3
    #cur.execute("DELETE FROM Больничные_листы WHERE id_сотрудника = (SELECT id FROM Анкеты WHERE должность = 'Менеджер')")
#4
    #cur.execute("DELETE FROM Больничные_листы WHERE id_сотрудника = (SELECT id FROM Анкеты WHERE отдел = 'Продаж')")
#5
    #cur.execute("DELETE FROM Больничные_листы WHERE id_сотрудника = (SELECT id FROM Анкеты WHERE пол = 'женский')")
#6
    ####cur.execute("DELETE FROM Больничные_листы WHERE id_сотрудника = (SELECT id FROM Анкеты WHERE julianday(дата_рождения) - julianday('2023-04-10') < -18000)")
#7
    #cur.execute("DELETE FROM Больничные_листы WHERE оплачен = FALSE")
#8
    #cur.execute("DELETE FROM Больничные_листы WHERE дата_окончания < '2023-04-14'")
#9
    #cur.execute("DELETE FROM Больничные_листы WHERE дата_начала > '2023-01-01'")
#10
    #cur.execute("DELETE FROM Больничные_листы WHERE дата_окончания > '2023-01-01'")
#12    
    ####cur.execute("DELETE FROM Больничные_листы WHERE id_сотрудника = (SELECT id FROM Анкеты WHERE фамилия LIKE 'С%')")
#13
    #cur.execute("DELETE FROM Больничные_листы WHERE id_сотрудника = (SELECT id FROM Анкеты WHERE должность = 'Менеджер' AND оплачен = FALSE)")
#14
    cur.execute("DELETE FROM Больничные_листы WHERE id_сотрудника = (SELECT id FROM Анкеты WHERE отдел = 'IT' AND дата_окончания > '2023-01-01')")