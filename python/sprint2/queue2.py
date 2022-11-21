class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class MyQueue:
    def __init__(self):
        self.head = None
        self.last = None
        self.fullsize = 0

    def put(self, value):
        node = Node(value)
        if not self.last:
            self.head = node
        else:
            self.last.next = node
        self.last = node
        self.fullsize += 1

    def get(self):
        if self.fullsize == 0:
            return print('error')
        if self.head != self.last:
            result = self.head.value
            self.head = self.head.next
            self.fullsize -= 1
            return print(result)
        result = self.head.value
        self.head = None
        self.last = None
        self.fullsize -= 1
        return print(result)

    def size(self):
        return print(self.fullsize)


n = int(input())
queue = MyQueue()
for c in range(n):
    command = input().split()
    if len(command) == 1:
        action = getattr(queue, command[0])
        action()
    else:
        action = getattr(queue, command[0])
        action(int(command[1]))
