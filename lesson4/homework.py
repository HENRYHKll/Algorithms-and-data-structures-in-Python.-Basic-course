# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# на примере пятой задачи из прошлого урока
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import cProfile
# import time
# import timeit
import random

def max_num(x):
    array = [random.randint(-100, -1) for _ in range(x)]
    max_num = array[0]
    for i in range(len(array) - 1):
        num = array[i]
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                num = array[i]
                break
        if num > max_num:
            max_num = num

# "work1.max_num(100)"
# 100 loops, best of 5: 186 usec per loop
# "work1.max_num(1000)"
# 100 loops, best of 5: 2.43 msec per loop
# "work1.max_num(10000)"
# 100 loops, best of 5: 59.9 msec per loop

# cProfile.run('max_num(100)')
# 1    0.000    0.000    0.000    0.000 hwork1.py:13(max_num)
# cProfile.run('max_num(1000)')
# 1    0.001    0.001    0.003    0.003 hwork1.py:13(max_num)
# cProfile.run('max_num(10000)')
# 1    0.041    0.041    0.062    0.062 hwork1.py:13(max_num)


def max_num_new(x):
    array = [random.randint(-100, -1) for _ in range(x)]
    max_num = float('-inf')
    for i in array:
        if max_num < i and i < 0:
            max_num = i

# work1.max_num_new(100)
# 100 loops, best of 5: 122 usec per loop
# work1.max_num_new(1000)
# 100 loops, best of 5: 1.2 msec per loop
# work1.max_num_new(10000)
# 100 loops, best of 5: 12.3 msec per loop

# cProfile.run('max_num_new(100)')
# 1    0.000    0.000    0.000    0.000 hwork1.py:47(max_num_new)
# cProfile.run('max_num_new(1000)')
# 1    0.000    0.000    0.002    0.002 hwork1.py:47(max_num_new)
# cProfile.run('max_num_new(10000)')
# 1    0.000    0.000    0.020    0.020 hwork1.py:47(max_num_new)


def max_num_new_f(x):
    array = [random.randint(-100, -1) for _ in range(x)]
    max(array)

# "work1.max_num_new_f(100)"
# 100 loops, best of 5: 119 usec per loop
# "work1.max_num_new_f(1000)"
# 100 loops, best of 5: 1.2 msec per loop
# "work1.max_num_new_f(10000)"
# 100 loops, best of 5: 12.4 msec per loop


# cProfile.run('max_num_new_f(100)')
# 1    0.000    0.000    0.000    0.000 hwork1.py:60(max_num_new_f)
# cProfile.run('max_num_new_f(1000)')
# 1    0.000    0.000    0.002    0.002 hwork1.py:60(max_num_new_f)
# cProfile.run('max_num_new_f(10000)')
# 1    0.000    0.000    0.019    0.019 hwork1.py:60(max_num_new_f)
# Второй и третий вариант решения по скорости одинаковые, но скорее всего третий вариант кушает больше ресурсов чем второй.

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile

def easy(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    # print(sieve)
    # res = [i for i in sieve if i != 0]
    # print(res)

# cProfile.run('easy(1000)')
# 1    0.000    0.000    0.000    0.000 hwork2.py:8(easy)
# cProfile.run('easy(10000)')
# 1    0.003    0.003    0.004    0.004 hwork2.py:8(easy)
# cProfile.run('easy(100000)')
# 1    0.039    0.039    0.044    0.044 hwork2.py:8(easy)

# "work2.easy(1000)"
# 100 loops, best of 5: 287 usec per loop
# "work2.easy(10000)"
# 100 loops, best of 5: 3.59 msec per loop
# "work2.easy(100000)"
# 100 loops, best of 5: 45.1 msec per loop



def easy_1(n):
    lst = []
    k = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
    # print(lst)

# cProfile.run('easy_1(1000)')
# 1    0.032    0.032    0.032    0.032 hwork2.py:37(easy_1)
# cProfile.run('easy_1(10000)')
# 1    4.262    4.262    4.262    4.262 hwork2.py:37(easy_1)
# cProfile.run('easy_1(100000)')
# 1  354.562  354.562  354.566  354.566 hwork2.py:37(easy_1)

# "work2.easy_1(1000)"
# 100 loops, best of 5: 28.7 msec per loop
# "work2.easy_1(10000)"
# 100 loops, best of 5: 3.37 sec per loop
# "work2.easy_1(100000)"
# Этого я дожидаться не стал :)




#Намного быстрее нахождение простых чисел с помощью решета Эратосфена.
# Есть вероятность что это связано с тем что во втором вариантемы добавляем в список значения
