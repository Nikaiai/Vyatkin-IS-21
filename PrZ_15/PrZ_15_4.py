import sqlite3
with sqlite3.connect('Аптека.db') as con:
    cur = con.cursor()
 #1
    #cur.execute("UPDATE Анкеты SET базовая_ставка = 41000.00 WHERE id = 1")
 #2    
    #cur.execute("UPDATE Анкеты SET отдел = 'PR' WHERE дата_рождения BETWEEN '1990-01-01' AND '2023-10-04' ")
 #3
    #cur.execute("UPDATE Анкеты SET дата_найма = '2023-04-10' WHERE id = 1")
 #4
    #cur.execute("UPDATE Больничные_листы SET причина = 'Болезнь' WHERE id = 341206")