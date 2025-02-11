class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.current_size = 0

    def push(self, x):
        if self.current_size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.current_size += 1
        else:
            return print('error')

    def pop(self):
        if self.current_size == 0:
            return print('None')
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.current_size -= 1
        return print(x)

    def peek(self):
        if self.current_size == 0:
            return print('None')
        return print(self.queue[self.head])

    def size(self):
        return print(self.current_size)


n = int(input())
max_que = int(input())
queue = MyQueueSized(max_que)
for c in range(n):
    command = input().split()
    if len(command) == 1:
        action = getattr(queue, command[0])
        action()
    else:
        action = getattr(queue, command[0])
        action(int(command[1]))