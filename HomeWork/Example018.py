# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X.
# Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

from random import randint
# size = int(input('Введите размер списка: '))
# nums_list = [randint(1, size) for _ in range(size)]
# print(*nums_list)
# print(nums_list.count(int(input('Введите искомое число: '))))

size = int(input('Количество чисел: '))
nums_list = [randint(1, size) for _ in range(size)]
print(*nums_list)
x = int(input('Заданное число: '))
near = [abs(nums_list[i]-x) for i in range(len(nums_list))]
print(nums_list[near.index(min(near))])

