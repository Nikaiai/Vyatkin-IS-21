# Вариант 5.
# Дан список размера N. Обнулить все его локальные максимумы (то есть числа, большие своих соседей).
import random

N = random.randrange(5, 20)
print(f"N = {N}")
a = [random.randrange(1, 21) for i in range(N)]
print(f"A: {a}")
for i in range(1, N - 1):
    if a[i - 1] < a[i] and a[i] > a[i + 1]:
        a[i] = 9999999
for i in range(1, N - 1):
    if a[i] == 9999999:
        a[i] = 0
print(f"Измененный A: {a}")
