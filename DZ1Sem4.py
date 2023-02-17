# Вычислить число c заданной точностью d 

import math


def leibniz(d):
    c = 0
    i = 0
    while True:
        c += (-1) ** i * 4 / (2 * i + 1)
        if abs(c - math.pi) <= 10 ** (-d):
            return c
        i += 1


d = float(input('Введите точность d: '))
print(f'Число c точностью {d} равно {leibniz(d)}')