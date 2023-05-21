# Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
import numpy as np
import random
a = np.random.randint(10, size=(3, 3))
print(f'Начальная матрица: \n {a} \n')
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] % 2 != 0:
            a[i][j] = 0
print(f'Измененная матрица: \n {a}')
