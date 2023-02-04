# Требуется вывести все целые степени двойки 
# (т.е. числавида 2k), не превосходящие числа N

user_input = int(input('Введите целое положительное число: '))
two_pow, power = 1, 1
while two_pow <= user_input:
    print(power, end=' ')
    two_pow = 2 ** power
    power += 1