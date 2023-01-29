# типы данных и переменная
# int, float, boolean, str, list, None

#value = None
#a = 123
#b = 1.23
#print(type(a))
#print(type(b))
# value = 12345
#print(type(value))
# s = 'hello world'

#print(s)
#print(a,'-' ,b,'-', s)
#print('{1} - {2} - {0}'.format(a, b, s))
#print(f'{a} - {b} - {s}')

#f = True
#print(f)

# list = ['1','2','3']
# col = ['hello', 1, 2, 3, 4.5, True]
# print(list)
# print(col)


# print('Введите a');
# a  = int(input())
# print('Введите b');
# b = int(input())
# print(a, ' + ' , b, ' = ', a+b)
# print('{} {}'.format(a, b))

# a = 1.312312313
# b = 3
# c = round(a * b, 5) # round математическое округление
# print(c)
# a = 3
# a += 5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# кое-что ещё: is, is not, in, not in

# f = [1,2,3,4]
# print(f)

# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции: if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Кот':
#     print('ты хуесос нутельный')
# elif username == 'Мальцев':
#     print(' Ты лучше Кота, а кот пэс ебаный')

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)

# Управляющие конструкции 
# for

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i**2)

# Функции - фрагмент программы, используемый многокократно

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print (f(arg))
print(type(f(arg)))
