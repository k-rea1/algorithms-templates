# ID: 75833067

"""
Задание связано с обратной польской нотацией, в которой операнды расположены
перед знаками операций. Для решения реализован класс типа Стэк, в котором
обрабатывается каждый элемент принятой обратной польской нотации и результат
каждой итерации вычислений добавляется в верхний элемент стэка.

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

ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
        }


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
        Если передано число, оно добавляется в стэк. Если передан знак
        операции, эта операция производится над последними двумя элементами
        стэка, после чего эти элементы удаляются, а результат операции
        добавляется в стэк.
        """
        if item in ops.keys():
            if self.len > 1:
                result = ops[item](self.items[-2], self.items[-1])
                self.items.pop()
                self.items.pop()
                self.items.append(result)
                self.len -= 1

        else:
            self.items.append(int(item))
            self.len += 1


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
"""

input = input().split()
for i in input:
    MyStack.push(i)
print(MyStack.pop())
