# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

def simpleNumber(n):
    flag = True
    for i in range(2, n):
        if n % i !=0:
            continue
        else:
            flag = False
            break
    return flag

print(simpleNumber(4))
