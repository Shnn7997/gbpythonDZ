# Крестики-Нолики

import random


board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board():
    print(board[0], "|", board[1], "|", board[2])
    print("----------")
    print(board[3], "|", board[4], "|", board[5])
    print("----------")
    print(board[6], "|", board[7], "|", board[8])


def player_choice():
    choice = int(input("Введите цифру от 1 до 9: "))
    if board[choice - 1] != "X" and board[choice - 1] != "O":
        board[choice - 1] = "X"
    else:
        print("Неверный ввод. Попробуйте еще раз")
        player_choice()


def bot_choice():
    choice = random.randint(0, 8)
    if board[choice] != "X" and board[choice] != "O":
        board[choice] = "O"
    else:
        bot_choice()


def check_win():
    if board[0] == board[1] == board[2] == "X" or \
            board[3] == board[4] == board[5] == "X" or \
            board[6] == board[7] == board[8] == "X" or \
            board[0] == board[3] == board[6] == "X" or \
            board[1] == board[4] == board[7] == "X" or \
            board[2] == board[5] == board[8] == "X" or \
            board[0] == board[4] == board[8] == "X" or \
            board[2] == board[4] == board[6] == "X":
        print("Вы победили!")
        return True
    elif board[0] == board[1] == board[2] == "O" or \
            board[3] == board[4] == board[5] == "O" or \
            board[6] == board[7] == board[8] == "O" or \
            board[0] == board[3] == board[6] == "O" or \
            board[1] == board[4] == board[7] == "O" or \
            board[2] == board[5] == board[8] == "O" or \
            board[0] == board[4] == board[8] == "O" or \
            board[2] == board[4] == board[6] == "O":
        print("Вы проиграли!")
        return True
    else:
        return False


def main():
    print("Добро пожаловать в игру Крестики-Нолики")
    print("Выберите режим игры")
    print("1. Человек против человека")
    print("2. Человек против бота")
    mode = int(input())
    if mode == 1:
        while True:
            draw_board()
            player_choice()
            if check_win():
                break
            draw_board()
            player2_choice()
            if check_win():
                break
    elif mode == 2:
        while True:
            draw_board()
            player_choice()
            if check_win():
                break
            draw_board()
            bot_choice()
            if check_win():
                break

main()