# ID: 75832779

"""
Реализована структура данных Дек с возможностью добавлять возвращать элементы
с обеих концов очереди. При реализации использован кольцевой буфер.

"""


class Deque:
    def __init__(self, n):
        self.__queue = [None] * n
        self.__max_n = n
        self.__head = 0
        self.__tail = 0
        self.__current_size = 0

    def push_back(self, x):
        """
        добавить элемент в конец дека. Если в деке уже находится максимальное
        число элементов, вывести ошибку.
        """
        if self.__current_size != self.__max_n:
            self.__queue[self.__tail] = x
            self.__tail = (self.__tail + 1) % self.__max_n
            self.__current_size += 1
        else:
            raise Exception('Full deque')

    def push_front(self, x):
        """
        добавить элемент в начало дека. Если в деке уже находится максимальное
        число элементов, вывести ошибку.
        """
        if self.__current_size != self.__max_n:
            self.__queue[self.__head-1] = x
            self.__head = (self.__head - 1) % self.__max_n
            self.__current_size += 1
        else:
            raise Exception('Full deque')

    def pop_front(self):
        """
        вывести первый элемент дека и удалить его. Если дек был пуст,
        то вывести ошибку.
        """
        if self.__current_size == 0:
            raise Exception('Empty deque')
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_n
        self.__current_size -= 1
        return print(x)

    def pop_back(self):
        """
        вывести последний элемент дека и удалить его. Если дек был пуст,
        то вывести ошибку.
        """
        if self.__current_size == 0:
            raise Exception('Empty deque')
        x = self.__queue[self.__tail-1]
        self.__queue[self.__tail-1] = None
        self.__tail = (self.__tail - 1) % self.__max_n
        self.__current_size -= 1
        return print(x)

    def len(self):
        return self.__current_size


"""
В первой строке записано количество команд n — целое число.
Во второй строке записано число — максимальный размер дека.
В следующих n строках записана одна из команд:
- push_back(value)
- push_front(value)
- pop_front()
- pop_back()

Результат выполнения каждой команды выводится на отдельной строке.
Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.

Пример 1:
Ввод
4
4
push_front 861
push_front -819
pop_back
pop_back

Вывод
861
-819

Пример 2
Ввод
6
6
push_front -201
push_back 959
push_back 102
push_front 20
pop_front
pop_back

Вывод
20
102

"""

if __name__ == '__main__':

    n = int(input())
    max_que = int(input())
    MyDeque = Deque(max_que)
    for c in range(n):
        command = input().split()
        if len(command) == 1:
            action = getattr(MyDeque, command[0])
            try:
                action()
            except Exception:
                print('error')
        else:
            action = getattr(MyDeque, command[0])
            try:
                action(int(command[1]))
            except Exception:
                print('error')
