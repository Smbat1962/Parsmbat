class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insertAtBegin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.value,end=" ")
            current_node = current_node.next

    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    def insertAtIndex(self, value, index):
        new_node = Node(value)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(value)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

llist = Linkedlist()
llist.insertAtBegin('a')
llist.insertAtBegin('b')
llist.insertAtBegin('c')
llist.insertAtBegin('d')
llist.printLL()
llist.insertAtEnd('w')
print()
llist.printLL()
print()
llist.insertAtIndex("z",3)
llist.printLL()