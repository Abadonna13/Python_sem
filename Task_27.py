# Хакер Василий получил доступ к классному журналу и хочет заменить все
# свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки
# Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

from random import randint

n = int(input("Введите номер элемента: "))
list_v = []
for i in range(n):
    list_v.append(randint(1, 5))
print(list_v)

min_ = min(list_v)
max_ = max(list_v)
for i in range(len(list_v)):
    if list_v[i] == max_:
        list_v[i] = min_
print(list_v)

