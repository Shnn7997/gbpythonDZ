# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.




import random


def generate_polynomial():
    polynomial = []
    for i in range(random.randint(2, 5)):
        polynomial.append(random.randint(-10, 10))
    return polynomial

polynomial_1 = generate_polynomial()
polynomial_2 = generate_polynomial()

with open('polynomial_1.txt', 'w') as file_1:
    file_1.write(str(polynomial_1))

with open('polynomial_2.txt', 'w') as file_2:
    file_2.write(str(polynomial_2))

polynomial_sum = [x + y for x, y in zip(polynomial_1, polynomial_2)]

with open('polynomial_sum.txt', 'w') as file_sum:
    file_sum.write(str(polynomial_sum))