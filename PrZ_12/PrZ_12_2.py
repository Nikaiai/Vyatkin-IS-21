# Вариант 5
# Составить генератор (yield), который переведет символы строки из нижнего
# регистра в верхний.
def lower_to_big(stroka):
    for i in stroka:
        yield i.upper()


text = input('Введите текст: ')
print(''.join(lower_to_big(text)))
