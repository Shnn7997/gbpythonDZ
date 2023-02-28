import csv
import json

# Функция для добавления записи
def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone_number = input('Введите номер телефона: ')

    contact = {
        'name': name,
        'surname': surname,
        'phone_number': phone_number
    }

    contacts.append(contact)
    print('Запись добавлена')


# Функция для поиска записи
def find_contact():
    search_name = input('Введите имя для поиска: ')
    for contact in contacts:
        if contact['name'] == search_name:
            print(f"Имя: {contact['name']}, Фамилия: {contact['surname']}, Номер телефона: {contact['phone_number']}")
            break
    else:
        print('Запись не найдена')


# Функция для редактирования записи
def edit_contact():
    search_name = input('Введите имя для редактирования: ')
    for contact in contacts:
        if contact['name'] == search_name:
            contact['name'] = input('Введите новое имя: ')
            contact['surname'] = input('Введите новую фамилию: ')
            contact['phone_number'] = input('Введите новый номер телефона: ')
            print('Запись отредактирована')
            break
    else:
        print('Запись не найдена')


# Функция для удаления записи
def delete_contact():
    search_name = input('Введите имя для удаления: ')
    for contact in contacts:
        if contact['name'] == search_name:
            contacts.remove(contact)
            print('Запись удалена')
            break
    else:
        print('Запись не найдена')


# Функция для экспорта данных в формате json
def export_json():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)
    print('Данные экспортированы в формате json')


# Функция для экспорта данных в формате csv
def export_csv():
    with open('contacts.csv', 'w') as file:
        fields = ['name', 'surname', 'phone_number']
        writer = csv.DictWriter(file, fields, delimiter=';')
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)
    print('Данные экспортированы в формате csv')


# Функция для импорта данных из формата json
def import_json():
    with open('contacts.json') as file:
        global contacts
        contacts = json.load(file)
    print('Данные импортированы из формата json')


# Функция для импорта данных из формата csv
def import_csv():
    with open('contacts.csv') as file:
        reader = csv.DictReader(file, delimiter=';')
        global contacts
        contacts = list(reader)
    print('Данные импортированы из формата csv')


# Функция для вывода всех записей
def show_contacts():
    for contact in contacts:
        print(f"Имя: {contact['name']}, Фамилия: {contact['surname']}, Номер телефона: {contact['phone_number']}")


# Функция для вывода приветственного меню
def show_menu():
    print('1. Добавить запись')
    print('2. Найти запись')
    print('3. Редактировать запись')
    print('4. Удалить запись')
    print('5. Экспорт данных в формате json')
    print('6. Экспорт данных в формате csv')
    print('7. Импорт данных из формата json')
    print('8. Импорт данных из формата csv')
    print('9. Показать все записи')
    print('0. Выход')


# Переменная для хранения записей
contacts = []

# Основной цикл программы
while True:
    show_menu()
    choice = input('Выберите пункт меню: ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        find_contact()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        export_json()
    elif choice == '6':
        export_csv()
    elif choice == '7':
        import_json()
    elif choice == '8':
        import_csv()
    elif choice == '9':
        show_contacts()
    elif choice == '0':
        break
        
    show_menu()