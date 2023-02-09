# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input())
num_str = str(num)

num_int = int(num_str.split('.')[0])
num_float = int(num_str.split('.')[1])

sum_int = 0
while num_int > 0:
    sum_int += num_int % 10
    num_int //= 10

sum_float = 0
while num_float > 0:
    sum_float += num_float % 10
    num_float //= 10

print(sum_int + sum_float)