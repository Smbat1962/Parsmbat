class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.head.next = new_node
            self.head = new_node

    def show_list(self):
        current_element = self.tail
        while current_element:
            print(current_element.value,end=" ")
            current_element = current_element.next

    def add_end(self,value):
        new_node = Node(value)
        new_node.next = self.tail
        self.tail = new_node 

    def insert_index(self, value, index):
        new_node = Node(value)
        current_element = self.tail
        position = 0
        if index == 0:
            self.add_end(value)
        while (current_element != None and position+1 != index):
                position += 1
                current_element = current_element.next
        if current_element != None:
            new_node.next = current_element.next
            current_element.next = new_node
        else:
            print("Index not present")


    def size_list(self):
        current_element = self.tail
        size = 0
        while current_element:
            size += 1
            current_element = current_element.next
        return size
    
    def remove_last_node(self):
        if self.tail == None:
           return
        self.tail = self.tail.next

    def remove_first_node(self):
        if self.tail is None:
            return
        current_node = self.tail
        while(current_node.next.next):
            current_node = current_node.next
        current_node.next = None

    def remove_penultimate_node(self):
        if self.tail == None:
           return
        self.tail.next = self.tail.next.next

    def remove_second_node(self):
        if self.tail is None:
            return
        current_node = self.tail
        while(current_node.next.next.next):
            current_node = current_node.next
        current_node.next = current_node.next.next

def method(): 
    print("Linkedlist")
        
        

    
def main():   
    linked_list = Linkedlist()
    linked_list.add("a")
    linked_list.add("b")
    linked_list.add("c")
    linked_list.add("x")
    linked_list.add("y")
    linked_list.add("wq")
    linked_list.add("opl")
    linked_list.add("vof")
    linked_list.add_end("ttf")
    linked_list.show_list()
    print(linked_list.size_list())
    linked_list.insert_index("Z", 2)
    linked_list.show_list()
    print(linked_list.size_list())
    linked_list.remove_last_node()
    print("\nafter remove last element")
    linked_list.show_list()
    linked_list.remove_first_node()
    print("\nafter remove first element")
    linked_list.show_list()
    linked_list.remove_penultimate_node()
    print("\nafter remove penultimate element")
    linked_list.show_list()
    linked_list.remove_second_node()
    print("\nafter remove second element")
    linked_list.show_list()

if __name__ == "__main__": 
    main()