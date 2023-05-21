from random import randint
a = []
a2 = []
for i in range(randint(10, 20)):
    a.append(randint(-20, 20))
t = 0
for i in range(len(a)):
    t += i
for i in range(len(a)):
    d = (a[i]*min(a))
    a2.append(d)
b = str(a)
b2 = str(a2)
c = (f'Исходые данные: {b} \nКоличество элементов: {len(b)} \nСумма элементов: {t}'
     f' \nЭлементы, умноженные на минимальный элемент: {a2}')
print(c)
f3 = open('data.txt', 'w')
f3.writelines(c)
f3.close()
