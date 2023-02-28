# Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

students = {}

def main_menu():
    print('Добро пожаловать в информационную систему студентов ВУЗа!')
    print('Выберите действие:')
    print('1. Добавить студента')
    print('2. Редактировать данные студента')
    print('3. Удалить студента')
    print('4. Вывести список студентов')
    print('5. Выход')
    choice = int(input('Ваш выбор: '))
    if choice == 1:
        add_student()
    elif choice == 2:
        edit_student()
    elif choice == 3:
        remove_student()
    elif choice == 4:
        show_students()
    elif choice == 5:
        print('До свидания!')
    else:
        print('Неверный выбор!')
        main_menu()

def add_student():
    name = input('Введите имя студента: ')
    if name in students:
        print('Такой студент уже существует!')
        main_menu()
    else:
        students[name] = []
        print('Студент успешно добавлен!')
        main_menu()

def edit_student():
    name = input('Введите имя студента: ')
    if name in students:
        print('Введите оценки студента через пробел: ')
        grades = list(map(int, input().split()))
        students[name] = grades
        print('Данные студента успешно отредактированы!')
        main_menu()
    else:
        print('Такого студента не существует!')
        main_menu()

def remove_student():
    name = input('Введите имя студента: ')
    if name in students:
        del students[name]
        print('Студент успешно удален!')
        main_menu()
    else:
        print('Такого студента не существует!')
        main_menu()

def show_students():
    for name, grades in students.items():
        print(f'Студент {name}: {grades}')
    main_menu()

main_menu()