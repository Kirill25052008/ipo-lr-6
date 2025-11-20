#Вариант 3

a = False

while a == False:

    count_of_rows = int(input("Введите положительное число:"))

    if count_of_rows < 1:
        print("Ошибка!!!")
        print("---------------------------------")
        continue
    else:
        break

print(f"Введите {count_of_rows} стро(к/у/и)")

i = 0
list = []

for _ in range(count_of_rows):
    line = input(f"Введите строку № {i + 1} : ")
    i += 1
    list.append(line)

text = "\n".join(list) # Объединяем строки в тнкст

words = text.split() # Разбиваем текст на слова
un_words = set(words) # Находим уникальные слова
count = len(un_words) # Находим количество уникальных слов

print(f"Количество уникальных слов = {count}")
