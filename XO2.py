# Крестики-нолики с PIP

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Создаем функцию для вывода игрового поля
def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+---+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+---+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# Создаем функцию для проверки введенных данных
def check_input(player_input):
    if player_input.isdigit():
        if int(player_input) in range(1,10):
            return True
        else:
            return False
    else:
        return False

# Создаем функцию для проверки победителя
def check_winner(board):
    # Проверяем строки
    if board[0] == board[1] == board[2]:
        return board[0]
    elif board[3] == board[4] == board[5]:
        return board[3]
    elif board[6] == board[7] == board[8]:
        return board[6]
    # Проверяем столбцы
    elif board[0] == board[3] == board[6]:
        return board[0]
    elif board[1] == board[4] == board[7]:
        return board[1]
    elif board[2] == board[5] == board[8]:
        return board[2]
    # Проверяем диагонали
    elif board[0] == board[4] == board[8]:
        return board[0]
    elif board[2] == board[4] == board[6]:
        return board[2]
    else:
        return None

# Задаем игровое поле
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Задаем переменные для игроков
player_1 = 'X'
player_2 = 'O'

# Задаем переменную для хода игрока
player_turn = player_1

# Задаем переменную для проверки продолжения игры
game_on = True

# Выводим игровое поле
print_board(board)

# Начинаем игру
while game_on:
    # Запрашиваем ввод игрока
    player_input = input('Игрок ' + player_turn + ', введите номер клетки: ')
    
    # Проверяем введенные данные
    if check_input(player_input):
        # Проверяем, занята ли клетка
        if board[int(player_input)-1] != player_1 and board[int(player_input)-1] != player_2:
            # Записываем введенные данные
            board[int(player_input)-1] = player_turn
            # Выводим игровое поле
            print_board(board)
            # Проверяем победителя
            winner = check_winner(board)
            # Если победитель есть
            if winner:
                # Выводим сообщение о победе
                print('Победил игрок ' + winner)
                # Завершаем игру
                game_on = False
            # Если победителя нет
            else:
                # Меняем игрока
                if player_turn == player_1:
                    player_turn = player_2
                else:
                    player_turn = player_1
        # Если клетка занята
        else:
            # Выводим сообщение об ошибке
            print('Клетка уже занята!')
    # Если данные введены неверно
    else:
        # Выводим сообщение об ошибке
        print('Введено неверное значение!')