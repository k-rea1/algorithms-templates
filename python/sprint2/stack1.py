class StackMax:
    def __init__(self):
         self.items = []

    def push(self, item):
         self.items.append(item)

    def pop(self):
         if len(self.items) == 0:
             return print('error')
         return self.items.pop()

    def get_max(self):
         if len(self.items) == 0:
             return print('None')
         return print(max(self.items))
     

stack = StackMax()
n = int(input())
for c in range(n):
    command = input().split()
    if len(command) == 1:
        action = getattr(stack, command[0])
        action()
    else:
        action = getattr(stack, command[0])
        action(int(command[1]))