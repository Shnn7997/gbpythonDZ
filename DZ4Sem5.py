# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = int(input('Введите степень многочлена: '))

coefficients = [random.randint(0, 100) for _ in range(k + 1)]

with open('polynomial.txt', 'w') as f:
    for i in range(k + 1):
        if i == 0:
            f.write(str(coefficients[i]))
        else:
            f.write(f' + {coefficients[i]}x^{i}')

print(f'Коэффициенты многочлена степени {k} записаны в файл polynomial.txt')