class Stack:
    def __init__(self):
        self.lst = []

    def push(self, value):
        self.lst.append(value)

    def pop(self):
        return self.lst.pop()
        
    def size(self):
        return len(self.lst)

    def is_empty(self):
        return not bool(self.size())

stack = Stack()
stack.push(1)
stack.push(3)
stack.push(0)
print(stack.lst)
print(stack.size())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.size())
print(stack.is_empty())