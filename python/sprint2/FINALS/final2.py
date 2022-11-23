# ID: 75833067

"""
Задание связано с обратной польской нотацией, в которой операнды расположены
перед знаками операций. Задача: вычислить выражение, переданное в виде
обратной польской нотации с использованием стэка.

Пример 1:
Ввод
2 1 + 3 *
Вывод
9

Пример 2:
Ввод
7 2 + 4 * 2 +
Вывод
38

"""

import operator


class Stack:

    def __init__(self):
        self.__items = []
        self.__len = 0

    def pop(self):
        """
        Возвращает и удаляет верхний элемент стэка. Если стэк пустой,
        возвращает ошибку.
        """
        if self.__len == 0:
            raise Exception('Empty stack')
        self.__len -= 1
        return self.__items.pop()

    def push(self, item):
        """
        Добавляет элемент в стэк.
        """
        self.__items.append(item)
        self.__len += 1

    def length(self):
        """
        Возвращает размер стэка.
        """
        return self.__len


ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
        }

MyStack = Stack()

"""
На вход в единственной строке даётся выражение, записанное в обратной польской
нотации. Числа и арифметические операции записаны через пробел.

На вход могут подаваться операции: +, -, *, / и числа

На выходе - результат вычисления обратной польской нотации.
"""

if __name__ == '__main__':

    input = input().split()
    for i in input:
        if i in ops.keys():
            if MyStack.length() > 1:
                b = MyStack.pop()
                a = MyStack.pop()
                result = ops[i](a, b)
                MyStack.push(result)
        else:
            MyStack.push(int(i))
    print(MyStack.pop())
