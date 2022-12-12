# Вариант 5.
# Дан список А размера N и целые числа К и L (1 < K < L < N).
# Переставить в обратном порядке элементы списка, расположенные между элементами Аки Al, включая эти элементы.
import random

n = random.randrange(4, 10)
L = random.randrange(2, n + 1)
k = random.randrange(1, L)

a = [i + 1 for i in range(n)]
print(f"N = {n}")
print(f"L = {L}")
print(f"K = {k}")
print(f"A: {a}")
count = (L - k + 1) // 2
print(f"Кол-во элементов между AK и AL: {count}")
i = 0
while i < count:
    a[k - 1 + i], a[L - 1 - i] = a[L - 1 - i], a[k - 1 + i]
    i += 1

print(f"Измененная A: {a}")
