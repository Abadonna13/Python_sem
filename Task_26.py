# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# def mult(a,b):
#     if b == 0:
#         return 1
#     return a * mult (a,b-1)
#
# a = int(input("Введите А: "))
# b = int(input("Введите В: "))
#
# print(mult(a,b))

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1: # добавление этой строки может улучшить производительность функции в случае,
        # если она будет вызываться со степенью, равной 1, многократно или внутри других функций.
        return base
    else:
        return base * power(base, exponent-1)

base = int(input("Введите А: "))
exponent = int(input("Введите В: "))
print(power(base,exponent))