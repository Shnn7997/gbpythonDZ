# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.

lst = [int(i) for i in input("Введите список целых чисел через ',': ").split(',')]

for i in range(len(lst) // 2):
    print(lst[i] * lst[-i-1], end=' ')

