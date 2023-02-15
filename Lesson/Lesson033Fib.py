# ------------------ РЕКУРСИЯ--------------------
# Рекурсия — это функция, вызывающая сама себя.
# При описании рекурсии важно указать, когда функции надо
# остановиться и перестать вызывать саму себя. По-другому говоря, необходимо
# указать базис рекурсии


def fib(n):
    if n in[1,2]:
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i)) # Append () добавляет в конец списка элемент, переданный ему в качестве аргумента.
print(list_1)