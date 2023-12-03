class Queue:
    def __init__(self):
        self.lst = []

    def put(self,value):
        self.lst.append(value)

    def get(self):
        return self.lst.pop(0)
    
    def qsize(self):
        return len(self.lst)

    def empty(self):
        return not bool(self.qsize())
    
    def full(self):
        return bool(self.qsize())
    
    
queue = Queue()
queue.put('a')
queue.put('b')
queue.put('c')
print(queue.lst)
print(queue.qsize())
print(queue.empty())
print(queue.full())
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.lst)
print(queue.qsize())
print(queue.empty())
print(queue.full())
