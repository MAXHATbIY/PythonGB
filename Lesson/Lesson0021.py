# ############# ФУНКЦИИ ############## #


# import hello as h

# print(h.f(1))


# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5))

#-----------Передача любого количества аргументов в функцию


# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1', 'd', '2'))


# ------------ РЕКУРСИЯ -------------#

# def fib(n):
#     if n in[1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) 

# ------------- Кортежи --------------.!.
# Кортеж - неизменяемый "список"

# a = (3, 1, 41, 4)
# print(a)
# print(a[0])

# -------------- Cловари ----------#
# Неупорядоченные коллекции произвольных объектов с доступом
# по ключу

# dictionary = {}
# dictionary = \
#     {
#         'up': '^',
#         'left': '<-',
#         'right': '->'
#     }
# # print(dictionary)
# # print(dictionary['left'])

# # for k in dictionary.keys():
# for k in dictionary.values():
#     print(k)

# --------------- Множества ------------№

# colors = {'red', 'green', 'blue'}
# print (colors)
# colors.add('red')
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# print(c)
# u = a.union(b)
# print(u)
# i = a.intersection(b)
# print(i)
# dl = a.difference(b)
# print(dl)
# dr = b.difference(a)
# print(dr)

# q = a\
#     .union(b) \
#     .difference(a.intersection(b))
# print(q)


# ------------ СПИСКИ -----------#

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)
# print()

# list1[0] = 123
# list2[1] = 223
# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

list1 = [1, 2, 3, 4, 5]

print(list1.pop()) # удаление элемента из списка
print(list1)
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)

print(list1.insert(2, 11)) # добавление элемента в список на нужную позицию(позиция, элемент)
print(list1)

print(list1.append(12)) # добавление элемента в конец списка
print(list1)

