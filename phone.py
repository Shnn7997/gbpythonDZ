import csv
import json

# приветственное меню
def welcome_menu():
    print('Добро пожаловать в телефонный справочник!')
    print('Выберите действие:')
    print('1. Вывести список записей')
    print('2. Добавить запись')
    print('3. Удалить запись')
    print('4. Импорт данных из файла')
    print('5. Экспорт данных в файл')
    print('6. Выход')
    choice = int(input('Введите номер действия: '))
    return choice

# вывод списка записей
def print_records(records):
    print('Список записей:')
    for record in records:
        print(f'{record[0]}: {record[1]}')

# добавление записи
def add_record(records):
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    records.append([name, phone])
    print('Запись успешно добавлена!')

# удаление записи
def remove_record(records):
    name = input('Введите имя для удаления: ')
    for record in records:
        if record[0] == name:
            records.remove(record)
            print('Запись успешно удалена!')
            break
    else:
        print('Запись не найдена!')

# импорт данных из файла
def import_records(records):
    file_name = input('Введите имя файла: ')
    file_extension = file_name.split('.')[-1]
    if file_extension == 'csv':
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                records.append(row)
            print('Данные успешно импортированы!')
    elif file_extension == 'json':
        with open(file_name, 'r') as json_file:
            records.extend(json.load(json_file))
            print('Данные успешно импортированы!')
    else:
        print('Неизвестный формат файла!')

# экспорт данных в файл
def export_records(records):
    file_name = input('Введите имя файла: ')
    file_extension = file_name.split('.')[-1]
    if file_extension == 'csv':
        with open(file_name, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(records)
            print('Данные успешно экспортированы!')
    elif file_extension == 'json':
        with open(file_name, 'w') as json_file:
            json.dump(records, json_file)
            print('Данные успешно экспортированы!')
    else:
        print('Неизвестный формат файла!')

# основной цикл
def main():
    records = []
    while True:
        choice = welcome_menu()
        if choice == 1:
            print_records(records)
        elif choice == 2:
            add_record(records)
        elif choice == 3:
            remove_record(records)
        elif choice == 4:
            import_records(records)
        elif choice == 5:
            export_records(records)
        elif choice == 6:
            break

main()