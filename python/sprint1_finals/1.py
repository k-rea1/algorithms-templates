# ID: 74607927

"""
Для каждого числа во вводимой строке необходимо вывести расстояние от этого
числа до ближайшего нуля. Если число = 0, эта величина будет равна нулю - 
расстоянию до самого себя. Числа выводятся в одну строку и разделяются пробелами.

Формат ввода: В первой строке дана длина улицы —– n (1 ≤ n ≤ 10^6).
В следующей строке записаны n целых неотрицательных чисел — номера домов и
обозначения пустых участков на карте (нули). Гарантируется, что в
последовательности есть хотя бы один ноль. Номера домов (положительные числа)
уникальны и не превосходят 10^9.

Пример 1:
Ввод
5
0 1 4 9 0

Вывод
0 1 2 1 0

Пример 2:
Ввод
6
0 7 9 4 8 20

Вывод
0 1 2 3 4 5
""" 

from typing import List


def previous_zero_distance(numbers: List[int]) -> List[int]:
    """Функция получает на вход список чисел и возвращает для каждого числа
    его расстояние до ближайшего предыдущего нуля. Если первое число в списке
    равно нулю, вместо расстояния для этого числа возвращается длина списка"""
    
    length = len(numbers)
    distances = []
    for id, item in enumerate(numbers):
        if item == 0:
            distances.append(0)
        elif id == 0:
            distances.append(length)
        else:
            distances.append(distances[id-1]+1)
    return distances

def get_zero_distance(street: List[int], ) -> List[int]:
    """Функция возвращает список расстояний до ближайшего нуля для каждого числа во
    входящем списке. Если число = 0, эта величина будет равна нулю - расстоянию до
    самого себя."""
   
    left_to_right = previous_zero_distance(street)
    street.reverse()    
    right_to_left = previous_zero_distance(street)
    right_to_left.reverse()   
    distance = []
    for i in range(len(left_to_right)):
        distance.append(min(left_to_right[i], right_to_left[i]))
        
    return distance


def read_input() -> List[int]:
    n = int(input())
    street = list(map(int, input().strip().split()))
    return street

street = read_input()
print(" ".join(map(str, get_zero_distance(street))))