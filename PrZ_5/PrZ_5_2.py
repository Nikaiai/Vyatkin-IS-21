# Вариант 5.
# Описать функцию DigitCountSum(K, C, S), находящую количество С цифр целого положительного числа K,
# а также их сумму S (K - входной, С и S - выходные параметры целого типа).
# С помощью этой функции найти количество и сумму цифр для каждого из пяти данных целых чисел.
import random


def DigitCountSum(K, Result):
    s = str(K)
    n = len(s)
    _sum = 0
    for i in range(n):
        _sum += int(s[i])
    Result['C'] = n
    Result['S'] = _sum


R = {"C": None, 'S': None}
for i in range(5):
    K = random.randrange(0, 100)
    print(f"Число {i+1}: {K}")
    DigitCountSum(K, R)
    print(f"Количество цифр = ", R["C"])
    print('Сумма цифр = ', R['S'])
    print()
