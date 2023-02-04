

num_sum = int(input('Введите сумму двух чисел: '))
num_product = int(input('Введите произведение двух чисел: '))
c = 0
for i in range(num_sum):
    if c:
        break
    for j in range(num_product):
        if i + j == num_sum and i * j == num_product:
            print(f'первое число = {i}, второе число = {j}')
            print()
# способ через математику
x = int((num_sum + (num_sum ** 2 - 4 * num_product) ** 0.5) / 2)
y = int((num_sum - (num_sum ** 2 - 4 * num_product) ** 0.5) / 2)
print(f'первое число = {x}, второе число = {y}')