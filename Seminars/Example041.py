


from random import randint
num_list = [randint(1, 20) for _ in range(int(input('Введите размер массива: ')))]
print(*num_list)
for i in range(1, len(num_list) - 1):
    if num_list[i - 1] < num_list[i] and num_list[i + 1] < num_list[i]:
        print(num_list[i - 1], num_list[i], num_list[i + 1])
        
# "\n" - экранированная последовательность(вывод с новой строки)


