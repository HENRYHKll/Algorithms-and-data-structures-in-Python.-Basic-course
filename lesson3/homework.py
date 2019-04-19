# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
import random

array = [0] * 8

i = 2
while i < 100:
    j = 2
    while j < 10:
        if i % j == 0:
            array[j - 2] += 1
        j += 1
    i += 1
print(array)

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
# значениями 1, 4, 5, 6 (или 0, 3, 4, 5 – если индексация начинается с нуля), т.к.
# именно в этих позициях первого массива стоят четные числа.
import random

array = [random.randint(1, 10) for _ in range(10)]
new_array = []
idx = 0
for i in array:
    if not i % 2:
        new_array.append(idx)
    idx += 1
print(array)
print(new_array)

# 4. Определить, какое число в массиве встречается чаще всего.

import random

array = [random.randint(0, 10) for _ in range(100)]
print(array)
len(array)
num = array[0]
max_repeat = 1
for i in range(len(array) - 1):
    repeat = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            repeat += 1
    if repeat > max_repeat:
        max_repeat = repeat
        num = array[i]

if max_repeat > 1:
    print(f'{max_repeat} раз встречается число {num}')
else:
    print('Все элементы уникальны')
    
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

array = [random.randint(-100, -1) for _ in range(30)]
print(array)

max_num = array[0]
position = 0
for i in range(len(array) - 1):
    num = array[i]
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            num = array[i]
            break
    if num > max_num:
        max_num = num
        position = i
print(f'максимальное из отрицательных число{max_num} находится на позиции {position}')

# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

array = [random.randint(0, 10) for _ in range(10)]
print(array)

if array[0] > array[1]:
    max_num = array[0]
    min_num = array[1]
    min1 = 1
    max1 = 0
else:
    min_num = array[0]
    max_num = array[1]
    min1 = 0
    max1 = 1

for i in range(2, len(array)):
    if array[i] < array[min1]:
        min1 = i
        min_num = array[i]
    if array[i] > array[max1]:
        max1 = i
        max_num = array[i]
print(f'Минимальное число {min_num} под индексом {min1}')
print(f'Максимальное число {max_num} под индексом {max1}')

sum_num = 0
for i in range(min1+1,max1-1):
    sum_num += array[i]
print(f'Сумма элементов, находящихся между минимальным и максимальным элементами равна {sum_num}')

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

array = [random.randint(0, 30) for _ in range(30)]
if array[0] > array[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, len(array)):
    if array[i] < array[min1]:
        b = min1
        min1 = i
        if array[b] < array[min2]:
            min2 = b
    elif array[i] < array[min2]:
        min2 = i

print(array)
print(array[min1])
print(array[min2])
