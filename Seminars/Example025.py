# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2



n = input().split()
result = {}
for i in n:
    if i in result:
        print(f'{i}_{result [i]}', end = ' ')
    else:
        print(f'{i}_{0}', end = ' ')
    result [i] = result.get(i,0) + 1