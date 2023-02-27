# Функция сжатия
def compress():
    with open('calculator_logs.txt', 'r') as f_in:
        text = f_in.read()
    # Подсчитываем количество повторяющихся символов
    result = []
    count = 1
    prev_char = text[0]
    for char in text[1:]:
        if char == prev_char:
            count += 1
        else:
            result.append(prev_char + str(count))
            prev_char = char
            count = 1
    else:
        result.append(prev_char + str(count))
    # Записываем результат в файл
    with open('compress.txt', 'w') as f_out:
        f_out.write(''.join(result))
    with open('calculator_logs.txt', 'w') as f_out:
        f_out.write(''.join(result))

# Функция восстановления
def decompress():
    with open('compress.txt', 'r') as f_in:
        text = f_in.read()
    # Восстанавливаем исходный текст
    result = []
    for i in range(0, len(text), 2):
        result.append(text[i] * int(text[i + 1]))
    # Записываем результат в файл
    with open('calculator_logs.txt', 'w') as f_out:
        f_out.write(''.join(result))

# Выбираем действие
action = input('Введите действие: ')
if action == 'сжать':
    compress()
elif action == 'распаковать':
    decompress()
else:
    print('Неверное действие')