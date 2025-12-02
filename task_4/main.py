search_line = input("Введите строку для поиска: ")# Просим пользователя ввести строку для поиска

try:
    with open("text.txt", "r", encoding = "utf-8") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Файл с названием text.txt не найден!!!")
    exit()

list_of_lines = []

for i in lines:
    line = i.strip()
    if search_line in line:
        list_of_lines.append(line)

print(f"Строк найдено: {len(list_of_lines)}")

list_of_lines.sort(key=len)

for i in list_of_lines:
    print(i)
