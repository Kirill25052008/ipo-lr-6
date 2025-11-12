#Вариант 3

a = False

while a == False:

    count_of_rows = int(input("Введите положительное число:"))

    if count_of_rows < 1:
        print("Ошибка!!!")
        continue
    else:
        break

print(f"Введите {count_of_rows} стро(к/у/и)")
