# -*- coding: utf-8 -*-
# домашняя работа №2        Вриант №6



# задание №1
'''
Задача 6.1. Дан массив целых чисел nums и число k. Вернуть массив минимальных значений для каждого окна размера k.

Вход:  nums = [5, 3, 4, 2, 8, 1], k = 3
Выход: [3, 2, 2, 1]
'''
def look_min_const_win(sp, k):
    if len(sp) < k:
        return None

    result = []
#    stak = []
    left = 0

    for i in range(k, len(sp) + 1):
        result.append(min(sp[left:i]))
        left += 1

    return result



# задание №2
'''
Задача 6.2. Дан массив положительных целых чисел nums и число target. Найти длину наибольшего непрерывного подмассива с суммой, не превышающей target.

Вход:  nums = [1, 2, 3, 4, 5], target = 10
Выход: 4
Пояснение: [1, 2, 3, 4] имеет сумму 10
'''
def look_max_len(sp, target):
    suma = 0
    result, per_res = 0, 0 # хрнаим результат и переменный результат для конкретного прохода
    left = 0

    for right in range(len(sp)):
        suma += sp[right]   # добавляю следующий элемент
        per_res += 1    

        while suma > target:    # начинаю обрезать со старого конца, если перелимитили
            suma -= sp[left]
            left += 1   # сдвигаю левую часть, если перелимитили
            per_res -= 1    # уменьшаю, если перелемитили

        result = max(result, per_res)

    return result



# задача №3
'''
Задача 6.3. Дан массив целых чисел nums. Реализовать структуру, которая отвечает на запросы вида: найти сумму элементов на отрезке от индекса left до индекса right включительно. Запросов может быть много.

nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) = 1     // -2 + 0 + 3
sumRange(2, 5) = -1     //  3 + (-5) + 2 + (-1)
sumRange(0, 5) = -3
'''
def build_prefix(sp):
    prefix = [0] * (len(sp) + 1)
    for i in range(len(sp)):
        prefix[i+1] = prefix[i] + sp[i]
    return prefix


def sumRange(prefix, left, right):
    return prefix[right+1] - prefix[left]







print(look_min_const_win([5, 3, 4, 2, 8, 1], 3))
print(look_max_len([1, 2, 3, 4, 5], 10))
nums = [-2, 0, 3, -5, 2, -1]
prefix = build_prefix(nums)
print(sumRange(prefix, 0, 2))
print(sumRange(prefix, 2, 5))
print(sumRange(prefix, 0, 5))