# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while


# res = 1
# n = int(input())
# for i in range(1, n + 1):
#     res *= i
# print(res)

num = 5
i = 1
F = 1

while i <=num:
    F = F * i
    i = i + 1
print(F)