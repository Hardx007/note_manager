# импортируем библиотеку для работы с datime
from datetime import datetime

# создаем список для дальнейшего занесения верного результата и отображения пользователю

data_list = []

# Получаем текущую дату без учета времени

current_data = datetime.now().date()

# отображаем текущую дату

print('Текущая дата :',current_data.strftime("%d.%m.%Y"))

# создаем цикл, в котором корректно вводим дату завершения
while True:
    data_enter = input("Введите дату завершения заметки в формате [день.месяц.год] \n-> ")
    try :
        data_enter1 = datetime.strptime(data_enter, '%d.%m.%Y').date()
        break
    except ValueError:
        print("Дата введена неверно!")
        if data_enter[2] != '.' or data_enter[5]:
            print('Попробуйте снова ! '
                  '\nПри вводе используйте символ -> "." '
                  '\nФормат даты -> [день.месяц.год]')

# Рассчитываем разницу между введенной датой и датой окончания заметки

datetime_check = (data_enter1 - current_data ).days

# прописываем условия, верное заносится в список
if datetime_check == 0:
    data_list.append("Сегодня дата окончания заметки")
elif datetime_check > 0:
    data_list.append("Количество дней до окончания заметки -> "  f"{datetime_check}" )
elif datetime_check < 0:
    data_list.append("Количество дней с момента истечения срока заметки -> "  f"{-datetime_check}")


#  Выводим информацию на экран пользователя

print ("\nВы ввели следующие данные:")
print(data_list)
