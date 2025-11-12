#Вариант 3

import random

numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2]

rows = random.randint(4,8)
colums = random.randint(4,8)

matrix = [[random.choice(numbers) for _ in range(rows)] for _ in range(colums)]

for rows in matrix:
    print(" ".join(f"{element:>4}" for element in rows))

sum_of_elements = 0

for rows in matrix:
    for element in rows:
        if element % 3 == 0:
            sum_of_elements += element

print(f"Сумма элементов кратных 3: {sum_of_elements}")
