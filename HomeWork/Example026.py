# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def a_pow_b(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return a * a_pow_b(a, b - 1)


print(a_pow_b(int(input('Введите число: ')), int(input('Введите значение степени: '))))