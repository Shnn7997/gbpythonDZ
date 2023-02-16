# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

n = int(input('Введите число: '))

fibonacci = [0, 1]

for i in range(2, n + 1):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

for i in range(-n, 0):
    fibonacci.append(fibonacci[i + 1] - fibonacci[i + 2])

print(fibonacci)