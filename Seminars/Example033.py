# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random


# list1 = []
# for i in range(n):
#     list1.append(int(input("add next ")))
list1 = [random.randint(1, 5) for i in range(int(input("enter marks number = ")))]
print(list1)
maxMark = max(list1)
minMark = min(list1)

for i in range(len(list1)):
    if list1[i] == maxMark:
        list1[i] = minMark
print(list1)