class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.next = None
  
  
class HashTable: 
    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.table = [None] * capacity 
  
    def _hash(self, key): 
        return hash(key) % self.capacity 
  
    def insert(self, key, value): 
        index = self._hash(key) 
        if self.table[index] is None: 
            self.table[index] = Node(key, value) 
            self.size += 1
        else: 
            current = self.table[index] 
            while current: 
                if current.key == key: 
                    current.value = value 
                    return
                current = current.next
            new_node = Node(key, value) 
            new_node.next = self.table[index] 
            self.table[index] = new_node 
            self.size += 1

    def search(self, key): 
        index = self._hash(key) 
        current = self.table[index] 
        while current: 
            if current.key == key: 
                return current.value 
            current = current.next
        raise KeyError(key) 
    def show_hash_table(self,key): 
        index = self._hash(key)
        current = self.table[index]
        while current: 
            print(current.value) 
            current = current.next

    def remove(self, key): 
        index = self._hash(key)   
        previous = None
        current = self.table[index] 
        while current: 
            if current.key == key:
                if previous: 
                    previous.next = current.next
                else: 
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current 
            current = current.next
        raise KeyError(key)

    

  
if __name__ == '__main__': 
    ht = HashTable(10) 
    ht.insert(2, 3) 
    ht.insert(12, 2) 
    ht.insert(22, 5)  
    print(ht.search(2)) 
    ht.show_hash_table(2)
    ht.remove(22) 
    ht.show_hash_table(2) 