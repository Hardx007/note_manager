username     = input('Введите имя пользователя : ')
title1       = input("Введите 1 заголовок  : " )
title2       = input("Введите 2 заголовок : " )
title3       = input("Введите 3 заголовок : " )
title        = [title1, title2, title3]
content      = input('Введите описание заметки : ')
status       = input('Введите статус заметки : ')
created_date = input("Введите дату начала задачи в формате 20.12.2024: " )
issue_date   = input("Введите дату завершения задачи в формате 22.12.2024: " )

note = {
    "Ваше имя пользователя": username,
    "Описание заметки": content,
    "Заголовки": title,
    "Статус заметки": status,
    "Дата начала задания": created_date [:5],
    "Дата завершения задания": issue_date [:5]
}
print(f"Ваши введенные данные : ", note)
