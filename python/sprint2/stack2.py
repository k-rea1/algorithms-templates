class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        self.items.append(item)
        if len(self.items) == 1:
            self.max.append(item)
            return
        if item > self.max[-1]:
            self.max.append(item)
        else:
            self.max.append(self.max[-1])

    def pop(self):
        if len(self.items) == 0:
            return print('error')
        self.items.pop()
        self.max.pop()

    def get_max(self):
        if len(self.items) == 0:
            return print('None')
        return print(self.max[-1])


stack = StackMaxEffective()
n = int(input())
for c in range(n):
    command = input().split()
    if len(command) == 1:
        action = getattr(stack, command[0])
        action()
    else:
        action = getattr(stack, command[0])
        action(int(command[1]))