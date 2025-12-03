import random
import itertools

list_of_numbers = []

for _ in range(20):
    i = tuple(random.randint(-10,10) for _ in range(4))# создаём кортеж (tuple) из четырех случайных целых чисел, каждое из которых находится в диапазоне от -10 до 10 включительно
    list_of_numbers.append(i)

print(f"Первоначальный список рандомных кортежей: {list_of_numbers}")

print("---------------------------------------")

unique_combinations = set(tuple(sorted(tup)) for tup in list_of_numbers)# Находит уникальные комбинации элементов из существующего списка (list_of_numbers), игнорируя порядок элементов внутри каждого кортежа
unique_combinations_list = list(unique_combinations)# Записываем все уникальные комбтнации в новый список unique_combinations_list

print(f"Все уникальные комбинации: {unique_combinations_list}")

print("---------------------------------------")

a = False

while a == False:
    try:
        number_of_user = int(input("Введите число: "))
        a = True
    except ValueError:
        print("Это не число!!!!! Введите, пожалуйста, число: ")
        a = False

print("---------------------------------------")

count_of_groups = 0

for i in list_of_numbers:# Этот цикл перебирает элементы в списке list_of_numbers
    for j in itertools.combinations(i,4):# Для каждого элемента i, внутренний цикл использует функцию itertools.combinations() для создания всех возможных уникальных комбинаций из 4 элементов без повторений. Каждая такая комбинация присваивается переменной j
        if sum(j) < number_of_user:# Программа вычисляет сумму элементов в текущей комбинации j, а затем сравнивает с введённым с клавиатуры числом
            count_of_groups += 1

print(f"Количество пар чисел из исходного массива, чья сумма меньше заданного пользователем значения = {count_of_groups}")
