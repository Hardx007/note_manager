# 2.1 Вводим заголовки и создаем их список.

title , titles = (), []

# 2.2 Цикл while работает пока не выполнится условие: заголовок неравен Enter.

while title != "Enter":
    title = input("Введите заголовок : для завершения напишите [Enter] >> ")

# 2.3 Условия if выставлены по приоритету, 1 условие завершает цикл при вводе Enter.

    if title == "Enter":
        break
# 2.4 Условие завершает цикл при наличии пустого заголовка.

    elif title == "":
        break
# 2.5 При отсутствии заголовка в списке добавляем в конец.

    elif title not in list(titles):
        titles.append(title)

# 2.6 Если подзаголовок имеется в списке возвращаем пользователя на этап ввода заголовка с соответствующим пояснением.

    elif title in list(titles):
        title = input("Введенный заголовок уже есть в списке, введите другой для завершения напишите [Enter] >> ")


note = {"Заголовки": titles}

# 3. Выводим информацию на экран пользователя


print (f"Заголовки пользователя :" , note["Заголовки"])
