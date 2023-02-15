# ---------------- ФУНКЦИИ --------------------

# Функция — это фрагмент программы, используемый многократно

# ----------------    1    --------------------
# Необходимо создать функцию sumNumbers(n), которая будет считать
# сумму всех элементов от 1 до n.

# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa +=i
#     return summa

# a = sum_numbers(5, 'qwert')
# print(a)

# ---------------   2    -----------------------

def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', '1'))
print(sum_str('q', 'e', '1', 't', '6'))

