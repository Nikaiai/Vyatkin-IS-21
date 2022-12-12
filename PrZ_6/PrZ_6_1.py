# Вариант 6
# Даны целые числа N (>2), А и В.
# Сформировать и вывести целочисленный список размера 10,
# первый элемент которого равен А, второй равен В, а каждый последующий элемент равен сумме всех предыдущих.

import random
import math

A = random.randrange(0, 10)
B = random.randrange(0, 10)

print("A = ", A)
print("B = ", B)
a = [A, B]
for i in range(2, 10):
    x = a[i-2] + a[i-1]
    a.append(x)
print(a)
