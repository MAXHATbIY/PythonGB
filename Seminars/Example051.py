# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

# --------------- Вариант 1 -------------------#
# def same_by(charac, objects):
#     list_characteristic = [charac(i) for i in objects]
#     for i in range(len(list_characteristic) - 1):
#         if list_characteristic[i] != list_characteristic[i + 1]: return False
#     return True


# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

#------------------Вариант2--------------#

def same_by(characteristic, objects):
    list1 = list(filter(characteristic, objects))
    return len(objects) == len(list1)

values = [0, 2, 10, 6,]

if same_by(lambda x: x % 2 == 0, values):
    print("same")
else:
    print("different")