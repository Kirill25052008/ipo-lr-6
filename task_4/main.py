search_line = input("Введите строку для поиска: ")# Просим пользователя ввести строку для поиска

try:# Пробуем
    with open("text.txt", "r", encoding = "utf-8") as file:# Откыть файл text.txt на чтение
        lines = file.readlines()# В переменную lines строки файла, открытого ранее
except FileNotFoundError:# Если не удалось открыть файл, то будет ошибка FileNotFoundError и 
    print("Файл с названием text.txt не найден!!!")# Выводим этот текст
    exit()# И завершаем программу

list_of_lines = []# Создаём пустой список

for i in lines:
    line = i.strip()
    if search_line in line:
        list_of_lines.append(line)

print(f"Строк найдено: {len(list_of_lines)}")

list_of_lines.sort(key=len)

for i in list_of_lines:
    print(i)

