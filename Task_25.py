def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input("Введите номер элемента: "))
list_f = []
for i in range(3, n):
    list_f.append(fib(i - 2))
print(list_f)
