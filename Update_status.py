status_dict = {}

status_true = True
while status_true:
#3.2 Цикл While работает, пока его значение истинно
    note_status = input('Введите статус заметки: '
                        '\n"1" - выполнено'
                        '\n"2" - в процессе'
                        '\n"3" - отложено'
                        '\n-> ')
#3.3 Перебираем все возможные варианты ввода и выводим на экран пользователя результат в конце программы
    if note_status == '1' or note_status == 'выполнено':
        status_dict['Статус заметки'] = 'выполнено'
        break
    elif note_status == '2' or note_status == 'в процессе':
        status_dict['Статус заметки'] = 'в процессе'
        break
    elif note_status == '3' or note_status == 'отложено':
        status_dict['Статус заметки'] = 'отложено'
        break
    else:
        print('Неверный вариант ввода')


# 4. Выводим информацию на экран пользователя

print ("\nВы ввели следующие данные:")
print (f"Статус заметки :" , status_dict)
