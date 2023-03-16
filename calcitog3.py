import logging

logging.basicConfig(filename="calculator.log", level=logging.DEBUG)

def add(x, y):
    result = x + y
    logging.debug(f"{x} + {y} = {result}")
    return result

def subtract(x, y):
    result = x - y
    logging.debug(f"{x} - {y} = {result}")
    return result

def multiply(x, y):
    result = x * y
    logging.debug(f"{x} * {y} = {result}")

def divide(x, y):
    try:
        result = x / y
        logging.debug(f"{x} / {y} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Попытка деления на ноль")
        print("Ошибка: деление на ноль")

def power(x, y):
    result = x ** y
    logging.debug(f"{x} ** {y} = {result}")
    return result

def modulus(x, y):
    result = x % y
    logging.debug(f"{x} % {y} = {result}")
    return result

def conjugate(x):
    result = x.conjugate()
    logging.debug(f"Конъюгирование {x} = {result}")
    return result

def calculate(expression):
    try:
        result = eval(expression)
        print("Результат:", result)
    except SyntaxError:
        print("Ошибка: недопустимое выражение")

def main():
    while True:
        print("Выберите действие:")
        print("1. Вычислить")
        print("2. Помощь")
        print("3. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            expression = input("Введите выражение: ")
            calculate(expression)
        elif choice == "2":
            print("Калькулятор поддерживает следующие операции:")
            print("+ - сложение")
            print("- - вычитание")
            print("* - умножение")
            print("/ - деление")
            print("** - возведение в степень")
            print("% - остаток от деления")
            print("c - конъюгирование комплексного числа")
            print("Можно использовать скобки для задания приоритета операций")
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Ошибка: недопустимый выбор")

if __name__ == "__main__":
    main()