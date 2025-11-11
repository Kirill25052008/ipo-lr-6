#Вариант 3

import random

numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2]

rows = random.randint(4,8)
colums = random.randint(4,8)

matrix = [[random.choice(numbers) for _ in range(rows)] for _ in range(colums)]

print(matrix)

