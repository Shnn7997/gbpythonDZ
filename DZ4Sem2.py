import random


N = int(input("Введите число N: "))

lst = [random.randint(-N, N) for _ in range(N)]

with open('file.txt', 'w') as data:
    for i in range(N):
        data.write(str(i) + '\n')

with open('file.txt', 'r') as data:
    positions = [int(p) for p in data.read().split()]

res = 1
for p in positions:
    res *= lst[p]

print(f'Произведение элементов на указанных позициях: {res}')
