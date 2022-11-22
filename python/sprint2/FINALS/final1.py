# ID: 75691946

"""
Реализована структура данных Дек с возможностью добавлять возвращать элементы
с обеих концов очереди. При реализации использован кольцевой буфер.

"""


class QueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.current_size = 0

    def push_back(self, x):
        """
        добавить элемент в конец дека. Если в деке уже находится максимальное
        число элементов, вывести «error».
        """
        if self.current_size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.current_size += 1
        else:
            return print('error')

    def push_front(self, x):
        """
        добавить элемент в начало дека. Если в деке уже находится максимальное
        число элементов, вывести «error».
        """
        if self.current_size != self.max_n:
            self.queue[self.head-1] = x
            self.head = (self.head - 1) % self.max_n
            self.current_size += 1
        else:
            return print('error')

    def pop_front(self):
        """
        вывести первый элемент дека и удалить его. Если дек был пуст,
        то вывести «error».
        """
        if self.current_size == 0:
            return print('error')
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.current_size -= 1
        return print(x)

    def pop_back(self):
        """
        вывести последний элемент дека и удалить его. Если дек был пуст,
        то вывести «error».
        """
        if self.current_size == 0:
            return print('error')
        x = self.queue[self.tail-1]
        self.queue[self.tail-1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.current_size -= 1
        return print(x)


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

n = int(input())
max_que = int(input())
queue = QueueSized(max_que)
for c in range(n):
    command = input().split()
    if len(command) == 1:
        action = getattr(queue, command[0])
        action()
    else:
        action = getattr(queue, command[0])
        action(int(command[1]))
