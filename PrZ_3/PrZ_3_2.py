# Вариант 5.
# Мастям игральных карт присвоены порядковые номера: 1- пики, 2 - трефы, 3 - бубны, 4 - червы.
# Достоинству карт, старших десятки, присвоены номера: 11 - валет, 12 - дама, 13 - король, 14 - туз.
# Дано трехзначное число, в котором первая цифра указывает на масть, а вторые две на достоинство карты.
# Вывести соответствующее название карты вида «дама червей», «туз треф» и т.п.
card = input("Введите число: ")
a = (int(card[0]))
b = (int(card[1:3]))
while a > 0 and a < 5 and b < 15 and b > 10:
    if b == 11:
        print('Валет', end=" ")
    elif b == 12:
        print("Дама", end=" ")
    elif b == 13:
        print("Король", end=" ")
    elif b == 14:
        print("Туз", end=" ")
    if a == 1:
        print("Пик")
    elif a == 2:
        print("Треф")
    elif a == 3:
        print("Бубен")
    elif a == 4:
        print("Червей")
    break
else:
    print("Вы ввели неправильное число, перезапустите программу и попробуйте еще раз")
