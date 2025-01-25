MyList = [] # создаем список для хранения заметок


def user():  # Создаем функцию ввода имени пользователя
    while True:
        username = input('Введите имя пользователя : ')
        if any(note["Ваше имя пользователя"] == username for note in MyList):
            print("пользователь существует")
            continue
        return username


def content_1():  # Создаем функцию ввода описания
    while True:
        content = input("Введите описание заметки : ")
        if content == "":
            print("Нет описания, повторите ввод")
            continue
        return content


def date1():  # Создаем функцию учета даты окончания и текущей даты

    # импортируем библиотеку для работы с datime
    from datetime import datetime

    # создаем список для дальнейшего занесения верного результата и отображения пользователю

    data_list = []

    # Получаем текущую дату без учета времени

    current_data = datetime.now().date()

    # отображаем текущую дату

    print('Текущая дата :', current_data.strftime("%d.%m.%Y"))

    # создаем цикл, в котором корректно вводим дату завершения
    while True:
        data_enter = input("Введите дату завершения заметки в формате [день.месяц.год] \n-> ")
        try:
            data_enter1 = datetime.strptime(data_enter, '%d.%m.%Y').date()
            break
        except ValueError:
            print("Дата введена неверно!")

    # Рассчитываем разницу между введенной датой и датой окончания заметки

    datetime_check = (data_enter1 - current_data).days

    # прописываем условия, верное заносится в список
    if datetime_check == 0:
        data_list.append("Сегодня дата окончания заметки")
    elif datetime_check > 0:
        data_list.append("Количество дней до окончания заметки -> "  f"{datetime_check}")
    elif datetime_check < 0:
        data_list.append("Количество дней с момента истечения срока заметки -> "  f"{-datetime_check}")
    return data_list


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

def stat():  # Создаем функцию учета статуса
    # Изменяемый статус заметок

    status_dict = {}
    status_true = True
    while status_true:  # Цикл While работает, пока его значение истинно
        note_status = input('Введите статус заметки: '
                            '\n"1" - новая'
                            '\n"2" - в процессе'
                            '\n"3" - отложено'
                            '\n-> ')
        # Перебираем все возможные варианты ввода и выводим на экран пользователя результат в конце программы
        if note_status == '1' or note_status == 'новая':
            status_dict['Статус заметки'] = 'новая'
            break
        elif note_status == '2' or note_status == 'в процессе':
            status_dict['Статус заметки'] = 'в процессе'
            break
        elif note_status == '3' or note_status == 'отложено':
            status_dict['Статус заметки'] = 'отложено'
            break
        else:
            print('Неверный вариант ввода')
    while True:
        word_stat_ask = input("Хотите изменить статус? "
                                "\n Да "
                                "\n Нет"
                                "\n ->  ")
        if word_stat_ask.lower() == "да":
            print("Выберите новый статус заметки путем ввода значения от 1 до 3 ")
            new_stat = input(   '\n"1" - новая'
                                '\n"2" - в процессе'
                                '\n"3" - отложено'
                                '\n-> ')
            if new_stat == "1":
                status_dict['Статус заметки'] = 'новая'
                print(f"Статус заметки изменен на -> {status_dict['Статус заметки']}")
            elif new_stat == "2":
                status_dict['Статус заметки'] = 'в процессе'
                print(f"Статус заметки изменен на -> {status_dict['Статус заметки']}")
            elif new_stat == "3":
                status_dict['Статус заметки'] = 'отложено'
                print(f"Статус заметки изменен на -> {status_dict['Статус заметки']}")
        elif word_stat_ask.lower() == "нет":
            break
        else:
            print("Неверный ввод!")
            continue
    return status_dict

def note_del(): # функция удаления
    ask_key_to_del = input("Введите имя пользователя или описание заметки для удаления \n -> ")
    for note in MyList[:]:
        if note["Ваше имя пользователя"] == ask_key_to_del: # создаем переменную для удаления
            MyList.remove(note) # при совпадении имени = удаление
            print(f"--- Заметка пользователя" ,{note["Ваше имя пользователя"]}, "удалена ---")
        elif note["Описание заметки"] == ask_key_to_del:
            MyList.remove(note) # при совпадении описания = удаление
            print(f"--- Заметка пользователя" ,{note["Ваше имя пользователя"]}, "с описанием",{note["Описание заметки"]},"удалена ---")
        elif note ["Ваше имя пользователя"] != ask_key_to_del:
            print(f"--- Заметки с именем пользователя {note["Ваше имя пользователя"]} не обнаружено! ---")
        elif note["Описание заметки"] != ask_key_to_del:
            print(f"--- Заметки с описанием {note["Описание заметки"]} не обнаружено!--- ")
def show_note(): # функция для отображения заметок в формате списка
    if not MyList:
        print("--- Список пуст--- ")
    else:
        for note in MyList:
            print("---Заметка---")
            print(f"Пользователь: {note["Ваше имя пользователя"]}")
            print(f"Описание: {note["Описание заметки"]}")
            print(f"{note["Текущий статус заметки"]}")
            print(f"{note["Срок заметки"]}")
            print(f"Заголовки: {note["Заголовки"]}")

while True:  # создаем цикл для повторного запроса конкретного действия у пользователя после каждого прохождения
    # Выводим всю информацию на экран пользователю для дальнейшего взаимодействия

    print("\n--- Добро пожаловать в Менеджер заметок! ---")
    print("--- Главное меню ---")
    print("Список действий:")
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
            "Текущий статус заметки": stat(),
            "Срок заметки": date1(),
            "Заголовки": tite()
        }
        MyList.append(note)
        print("--- Заметка добавлена ---")
    # при вводе 2 отображается список заметок если такой имеется
    elif operation == "2":
        "\n"
        show_note()
    # при вводе 3 удаляется
    elif operation == "3":
        if not MyList:
            print("--- Список пуст ---")
        else:
            note_del()
    # Осуществляется выход из программы
    elif operation == "4":
        print("--- Выход из программы. ---")
        break
    else:
        print("--- Неверный выбор. Попробуйте снова. ---")
