#Вариант 3

list = [
    "Солнце медленно клонилось к горизонту, окрашивая небо в оранжевые и розовые тона.",
    "Белый парусник медленно плыл по глади озера.",
    "Привет, мир!!!",
    "Запах свежеиспеченного хлеба доносился из маленькой пекарни",
    "Алый закат украшает небосвод.",
    "Это задание было сделано на Python"
]

count_of_str_with_v = 0

for i in list:
    if "В" in list[0] or "в" in list[0]:
        count_of_str_with_v += 1
        break

for i in list:
    if "В" in list[1] or "в" in list[1]:
        count_of_str_with_v += 1
        break

for i in list:
    if "В" in list[2] or "в" in list[2]:
        count_of_str_with_v += 1
        break

for i in list:
    if "В" in list[3] or "в" in list[3]:
        count_of_str_with_v += 1
        break

for i in list:
    if "В" in list[4] or "в" in list[4]:
        count_of_str_with_v += 1
        break

for i in list:
    if "В" in list[5] or "в" in list[5]:
        count_of_str_with_v += 1
        break

print("Количество строк с буквой 'в'(или 'В') = ", count_of_str_with_v)
