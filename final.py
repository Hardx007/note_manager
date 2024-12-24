username     = input('Введите имя пользователя : ')
title1       = input("Введите 1 заголовок  : " )
title2       = input("Введите 2 заголовок : " )
title3       = input("Введите 3 заголовок : " )
title        = [title1, title2, title3]
content      = input('Введите описание заметки : ')
status       = input('Введите статус заметки : ')
created_date = input("Введите дату начала задачи в формате 20.12.2024: " )
issue_date   = input("Введите дату завершения задачи в формате 22.12.2024: " )

note = username, title, content, status, created_date, issue_date
note = {
    "Ваше имя пользователя": note[0],
    "Описание заметки": note[2],
    "Заголовки": note[1],
    "Статус заметки": note[3],
    "Дата начала задания": note[4][0:5],
    "Дата завершения задания": note[5][0:5]
}
print(f"Ваши введенные данные : ", note)