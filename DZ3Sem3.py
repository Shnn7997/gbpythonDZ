# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

a = [float(i) for i in input("Введите вещественные числа через пробел: ").split()]

min_val = 1
max_val = 0

for i in a:
    if i - int(i) > max_val:
        max_val = i - int(i)
    if i - int(i) < min_val:
        min_val = i - int(i)

print(round(max_val - min_val, 2))