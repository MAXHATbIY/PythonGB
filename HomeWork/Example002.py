# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов.
#  Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

s = int(input("Введите количество журавликов кратное шести: "))

if s % 6 == 0:
    pet = s // 6
    ser = pet
    kat = pet * 4
    print(s, " -> ", pet, kat, ser)
else:
    print("Введенное количество журавликов не подходит по условию задачи")