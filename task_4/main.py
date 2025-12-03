search_line = input("Введите строку для поиска: ")# Просим пользователя ввести строку для поиска

try:# Пробуем
    with open("text.txt", "r", encoding = "utf-8") as file:# Откыть файл text.txt на чтение
        lines = file.readlines()# В переменную lines записываем строки файла, открытого ранее
except FileNotFoundError:# Если не удалось открыть файл, то будет ошибка FileNotFoundError и 
    print("Файл с названием text.txt не найден!!!")# Выводим этот текст
    exit()# И завершаем программу

list_of_lines = []# Создаём пустой список

for i in lines:# Создаём цикл, который будет пробегаться по переменной lines
    line = i.strip()# В переменную line записываем предложения из строки lines, без пробелов
    if search_line in line:# Если переменная search_line есть в переменной line, то
        list_of_lines.append(line)# Записываем эту строку в созданный ранее список 

print(f"Строк найдено: {len(list_of_lines)}")# Выводим получившуюся длину списка

list_of_lines.sort(key=len)# Сортируем список в порядке их длины

for i in list_of_lines:# Создаём цикл, который будет пробегаться по списку list_of_lines (уже отсартированным)
    print(i)# И выводим его


