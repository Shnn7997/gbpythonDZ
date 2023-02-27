
# игра в 2021 конфету

import random

# Функция для игры человек-человек
def human_vs_human(candy):
    print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. За один ход можно забрать не более чем 28 конфет.')
    print('Первый ход определяется жеребьёвкой.')
    # Определяем первого игрока
    player1 = random.choice(['Игрок 1', 'Игрок 2'])
    player2 = 'Игрок 1' if player1 == 'Игрок 2' else 'Игрок 2'
    print(f'Первым ходит {player1}.')
    # Запускаем игру
    while candy > 0:
        print(f'На столе осталось {candy} конфет.')
        # Ход первого игрока
        if player1 == 'Игрок 1':
            candy_taken = int(input(f'{player1}, сколько конфет вы хотите взять? '))
            if candy_taken > 28:
                print('Вы не можете взять больше 28 конфет.')
                continue
            candy -= candy_taken
            player1, player2 = player2, player1
        # Ход второго игрока
        else:
            candy_taken = int(input(f'{player2}, сколько конфет вы хотите взять? '))
            if candy_taken > 28:
                print('Вы не можете взять больше 28 конфет.')
                continue
            candy -= candy_taken
            player1, player2 = player2, player1
    # Определяем победителя
    winner = player1 if candy == 0 else player2
    print(f'Победил {winner}.')

# Функция для игры человек-бот
def human_vs_bot(candy):
    print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. За один ход можно забрать не более чем 28 конфет.')
    print('Первый ход определяется жеребьёвкой.')
    # Определяем первого игрока
    player1 = random.choice(['Игрок', 'Бот'])
    player2 = 'Игрок' if player1 == 'Бот' else 'Бот'
    print(f'Первым ходит {player1}.')
    # Запускаем игру
    while candy > 0:
        print(f'На столе осталось {candy} конфет.')
        # Ход первого игрока
        if player1 == 'Игрок':
            candy_taken = int(input(f'{player1}, сколько конфет вы хотите взять? '))
            if candy_taken > 28:
                print('Вы не можете взять больше 28 конфет.')
                continue
            candy -= candy_taken
            player1, player2 = player2, player1
        # Ход второго игрока
        else:
            candy_taken = random.randint(1, 28)
            print(f'{player2} взял {candy_taken} конфет.')
            candy -= candy_taken
            player1, player2 = player2, player1
    # Определяем победителя
    winner = player1 if candy == 0 else player2
    print(f'Победил {winner}.')

# Запускаем игру
print('Добро пожаловать в игру с конфетами!')
mode = input('Выберите режим игры (1 - человек против человека, 2 - человек против бота): ')
if mode == '1':
    human_vs_human(2021)
elif mode == '2':
    human_vs_bot(2021)
else:
    print('Неверный режим игры.')