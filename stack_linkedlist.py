import linked_list_impoet

class Stack:
    def __init__(self):
        self.lst = linked_list_impoet.Linkedlist()

    def push(self, value):
        self.lst.add(value)

    def pop(self):
        return self.lst. remove_last_node()
        
    def size(self):
        print(self.lst.size_list())
    
    def show_stack(self):
        return self.lst.show_list()

    def is_empty(self):
        return not bool(self.lst.size_list())
def main():
    stack = Stack()
    stack.push(1)
    stack.push(3)
    stack.push(0)
    stack.show_stack()
    print()
    print(stack.is_empty())
    stack.size()
    stack.pop()
    stack.show_stack()
    print()
    print(stack.is_empty())
    stack.size()
    stack.pop()
    stack.show_stack()
    print()
    print(stack.is_empty())
    stack.size()
    stack.pop()
    stack.show_stack()
    print(stack.is_empty())
    stack.size()
    
    

    

if __name__ == "__main__":
    main()
