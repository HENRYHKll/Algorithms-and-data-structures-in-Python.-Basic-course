# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

# Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32

import string
import sys

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

# Вариант 1-1
a = input('Введите первый символ буквы: ')
b = input('Введите второй символ буквы: ')

list1 = string.ascii_lowercase

leter1 = list1.rfind(a) + 1
leter2 = list1.rfind(b) + 1

if leter1 > leter2:
    gap = leter1 - leter2
elif leter1 < leter2:
    gap = leter2 - leter1

print('Буква {} находится на '.format(a) + str(leter1) + ' месте')
print('Буква {} находится на '.format(b) + str(leter2) + ' месте')
print('Между буквами {} и {} {} буквы'.format(a, b, gap-1))

# Буква a находится на 1 месте
# Буква q находится на 17 месте
# Между буквами a и q 15 буквы
# type = <class 'str'>, size = 75, object = abcdefghijklmnopqrstuvwxyz
# type = <class 'int'>, size = 28, object = 1
# type = <class 'int'>, size = 28, object = 17
# type = <class 'int'>, size = 28, object = 16


# print(f'type = {type(list1)}, size = {sys.getsizeof(list1)}, object = {list1}')
# print(f'type = {type(leter1)}, size = {sys.getsizeof(leter1)}, object = {leter1}')
# print(f'type = {type(leter2)}, size = {sys.getsizeof(leter2)}, object = {leter2}')
# print(f'type = {type(gap)}, size = {sys.getsizeof(gap)}, object = {gap}')

# Вариант 1-2
first = ord(input('1-я буква: '))
second = ord(input('2-я буква: '))

first = first - ord('a') + 1
second = second - ord('a') + 1

print(f'Порядковый номер 1-ой буквы {first} 2-ой буквы {second}')
print(f'Число букв между введеными: {abs(first - second) - 1}')

# Порядковый номер 1-ой буквы 1 2-ой буквы 17
# Число букв между введеными: 15
# type = <class 'int'>, size = 28, object = 1
# type = <class 'int'>, size = 28, object = 17

# print(f'type = {type(first)}, size = {sys.getsizeof(first)}, object = {first}')
# print(f'type = {type(second)}, size = {sys.getsizeof(second)}, object = {second}')


# Вариант 1-1 конечно не оптимальный занимает гораздо больше памяти чем вариант 2
# В варианте 1-2 используется 4 объекта с общим размером 159 байт
# Когда в варианте 2 используется всего 2 объекта с общим размером всего 56 байт
# Разница практически в 3 раза


# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# Вариант 2-1
a = int(input('Введите номер буквы: '))
list1 = string.ascii_lowercase
if a > 26 or a < 1:
    print("Буквы с таким номером нет")
else:
    print(list1[a-1])
# Введите номер буквы: 4
# d
# type = <class 'int'>, size = 28, object = 4
# type = <class 'str'>, size = 75, object = abcdefghijklmnopqrstuvwxyz
# print(f'type = {type(a)}, size = {sys.getsizeof(a)}, object = {a}')
# print(f'type = {type(list1)}, size = {sys.getsizeof(list1)}, object = {list1}')

# Вариант 2-2
num = int(input('Введите номер буквы от 1 до 26: '))
o = ord('a')
num = o + num - 1

print(f'Эта буква {chr(num)}')
print(f'type = {type(num)}, size = {sys.getsizeof(num)}, object = {num}')
print(f'type = {type(o)}, size = {sys.getsizeof(o)}, object = {o}')
# Эта буква d
# type = <class 'int'>, size = 28, object = 100
# type = <class 'int'>, size = 28, object = 97

# Вариант 2-3
FIRST_LETTER = 96
num = int(input('Введите номер буквы от 1 до 26: '))
num = FIRST_LETTER + num
print(f'Эта буква {chr(num)}')
print(f'type = {type(FIRST_LETTER)}, size = {sys.getsizeof(FIRST_LETTER)}, object = {FIRST_LETTER}')
print(f'type = {type(num)}, size = {sys.getsizeof(num)}, object = {num}')
# Эта буква d
# type = <class 'int'>, size = 28, object = 96
# type = <class 'int'>, size = 28, object = 100


# Вариант 2-1 не оптималльный занимает 103 байта
# Вариант 2-2 хороший и занимает памяти столько же сколько 2-3 (занимают 56 байт)
# Но вариант 2-2 дольше отрабатывает по времени чем вариант 2-3

# def c1(num = 4):
#     o = ord('a')
#     num = o + num - 1
# "work1.c1()"
# 100 loops, best of 5: 218 nsec per loop

# def c2(num = 4):
#     FIRST_LETTER = 96
#     num = FIRST_LETTER + num
# "work1.c2()"
# 100 loops, best of 5: 141 nsec per loop
