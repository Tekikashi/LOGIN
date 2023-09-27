# Функция для регистрации новых студентов
def register_student():
    # Запрос данных о студенте
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    # Проверка, не существует ли уже такого логина
    with open("students.txt", "r") as file:
        existing_logins = [line.split()[2] for line in file.readlines()]
    
    if login in existing_logins:
        print("Пользователь с таким логином уже существует.")
    else:
        # Сохранение информации о новом студенте
        with open("students.txt", "a") as file:
            file.write(f"{first_name} {last_name} {login} {password}\n")
        print("Регистрация прошла успешно.")

# Функция для авторизации студентов
def login_student():
    # Запрос логина и пароля
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    # Проверка, есть ли такой логин и пароль в файле
    with open("students.txt", "r") as file:
        students_data = [line.split() for line in file.readlines()]
    
    for student in students_data:
        if student[2] == login and student[3] == password:
            print("Авторизация успешна.")
            return
    
    print("Неверный логин или пароль.")

# Главное меню для авторизованных пользователей
def main_menu():
    print("1. Просмотр личной информации")
    print("2. Изменение пароля")
    print("3. Выход")

    choice = input("Выберите опцию: ")

    if choice == "1":
        # Реализуйте здесь просмотр личной информации
        pass
    elif choice == "2":
        # Реализуйте здесь изменение пароля
        pass
    elif choice == "3":
        print("Выход...")
    else:
        print("Неверный выбор.")

# Главная функция
def main():
    while True:
        print("1. Регистрация")
        print("2. Авторизация")
        print("3. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            login_student()
            # Если авторизация успешна, вызываем меню для авторизованных пользователей
            main_menu()
        elif choice == "3":
            print("Выход...")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
