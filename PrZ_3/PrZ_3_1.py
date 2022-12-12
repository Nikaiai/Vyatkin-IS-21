a = input("Введите целое число: ") #Ввод первого числа
while type(a) != int: #
    try:
        a = int(a)
    except ValueError:
        print("Неверно введено число")
        a = input("Введите целое число: ")
b = input("Введите другое целое  число: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неверно введено число")
        b = input("Введите другое целое  число: ")
k = int
k = 0
if a > 0:
    k += 1
    print("Первое число больше нуля")
if b < -2:
    k += 1
    print("Второе число меньшнке двух")
if k<1 : print("Оба неравенства неверны")
if k==1 : print("Одно неравенство верно")
if k==2 : print("Оба неравенства верны")