import random

list_of_numbers = [i for i in range(0,25)]

count_of_positive_numbers = 0
count_of_negative_numbers = 0
count_of_zero_elements = 0

max = 0
min = 0

for i in list_of_numbers:
    i = random.randint(-50,50)
    print(i)

    if i > 0:
        count_of_positive_numbers += 1
    elif i < 0:
        count_of_negative_numbers += 1
    else:
        count_of_zero_elements += 1  

    if i > max:
        max = i
    elif i < min:
        min = i    

print(f"Количество положительных элементов = {count_of_positive_numbers}")
print(f"Количество отрицательных элементов = {count_of_negative_numbers}")
print(f"Количество нулевых элементов = {count_of_zero_elements}")
print("------------------------------------")
print(f"Максимальное число = {max}")
print(f"Минимальное число = {min}")
