n = input("Введите целое положительное число неравное 0: ")
while type(n) != int:
    try:
        n = int(n)
    except:
        print("Неправильное число")
        n = input("Введите целое положительное число неравное 0: ")
g = n
count = 0
while(n > 0):
    count = count + 1
    n = n // 10
print("Количество цифр равно:", count)
c = 0
while g>0:
    c = c + g % 10
    g = g // 10
print(f"Сумма цифр равна: {c}")