# Реализовать алгоритм перемешивания списка.


import random


def shuffle_list(list_):
    shuffled_list = list_.copy()
    for i in range(len(shuffled_list)):
        random_index = random.randint(0, len(shuffled_list) - 1)
        shuffled_list[i], shuffled_list[random_index] = shuffled_list[random_index], shuffled_list[i]
    return shuffled_list


list_ = [1, 2, 3, 4, 5]
print(shuffle_list(list_))




#2-вариант
lst = [random.randint(0, 50) for i in range(random.randint(5, 10))]
print(f"исходный список:\n {lst}")
random.shuffle(lst)
print(f"перемешанный список:\n{lst}")