# Задайте список из нескольких чисел с клавиатуры. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции 



list_numbers = list(map(int, input('Введите список чисел через пробел: ').split()))

sum_odd_numbers = 0

for i in range(len(list_numbers)):
    if i % 2 != 0:
        sum_odd_numbers += list_numbers[i]

print(f'Сумма элементов списка, стоящих на нечётной позиции: {sum_odd_numbers}')