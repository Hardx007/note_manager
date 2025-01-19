print("Добро пожаловать в Менеджер заметок!")
MyList = []


def user():  # Создаем функцию ввода имени пользователя

    username = input('Введите имя пользователя : ')
    return username


def content_1():  # Создаем функцию ввода описания
    content = input('Введите описание заметки : ')
    return content

def tite():  # Создаем функцию для формирования списков
    # Вводим заголовки и создаем их список.

    title, titles = (), []

    # Цикл while работает пока не выполнится условие: заголовок неравен Enter.

    while title != "Enter":
        title = input("Введите заголовок : для завершения напишите или нажмите -> [Enter] >> ")

        # Условия if выставлены по приоритету, 1 условие завершает цикл при вводе или нажатии Enter.

        if title == "Enter":
            break
        # Условие завершает цикл при наличии пустого заголовка.

        elif title == "":
            break
        # При отсутствии заголовка в списке добавляем в конец.

        elif title not in list(titles):
            titles.append(title)

        # Если подзаголовок имеется в списке возвращаем пользователя на этап ввода заголовка с соответствующим пояснением.

        elif title in list(titles):
            title = input(
                "Введенный заголовок уже есть в списке, введите другой для завершения напишите или нажмите -> [Enter] ")
    return titles

def note_del(): # функция удаления
    ask_key_to_del = input("Введите имя пользователя или описание заметки для удаления \n -> ")
    for note in MyList:
        if note["Ваше имя пользователя"] == ask_key_to_del: # создаем переменную для удаления
            MyList.remove(note) # при совпадении имени = удаление
            print(f"Заметка пользователя" ,{note["Ваше имя пользователя"]}, "удалена ")
        elif note["Описание заметки"] == ask_key_to_del:
            MyList.remove(note) # при совпадении описания = удаление
            print(f"Заметка пользователя" ,{note["Ваше имя пользователя"]}, "с описанием",{note["Описание заметки"]},"удалена ")

while True:  # создаем цикл для повторного запроса конкретного действия у пользователя после каждого прохождения
    # Выводим всю информацию на экран пользователю для дальнейшего взаимодействия

    print("\nВыберите действие:")
    print("1. Добавить заметку")
    print("2. Показать все заметки")
    print("3. Удалить заметку")
    print("4. Выйти")
    operation = input("Введите число от 1 до 4: -> ")
    # при вводе 1 - запускается программа
    if operation == "1":
        note = {
            "Ваше имя пользователя": user(),
            "Описание заметки": content_1(),
            "Заголовки": tite()
        }
        MyList.append(note)
    # при вводе 2 отображается список заметок если такой имеется
    elif operation == "2":
        if not MyList:
            print("---Список пуст---")
        else:
            print(*MyList)
    # при вводе 3 удаляется
    elif operation == "3":
        if not MyList:
            print("---Список пуст---")
        else:
            note_del()


    # Осуществляется выход из программы
    elif operation == "4":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")