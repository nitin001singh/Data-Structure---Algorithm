class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None



class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.keyTable = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        
        self.head.next = self.tail
        self.tail.prev = self.head 
        
        
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

        
    def append(self, node):
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node


    def get(self, key):
        if key in self.keyTable:
            node = self.keyTable[key]
            self.remove(node)
            self.append(node)
            return node.value
        
        return -1
        

    def put(self, key, value):
        
        if self.capacity == 0:
            return None
        
        if key in self.keyTable:
            self.remove(self.keyTable[key])
            
        node = Node(key, value)
        self.keyTable[key] = node
        self.append(node)
             
        if len(self.keyTable) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.keyTable[lru.key]
        

            
    def __str__(self):
        
        current = self.head
        result = ""
        while current:
            result += str(current.key) +":"+str(current.value) + " => "
            current = current.next
        
        result = result[:-4]
        
        print(self.keyTable)
        
        return result
            
        
        
lRUCache = LRUCache(2);
lRUCache.put(1, 1);   #// cache is {1=1}
lRUCache.put(2, 2); #// cache is {1=1, 2=2}
print(lRUCache)
lRUCache.get(1);    #// return 1
# print(lRUCache)
lRUCache.put(3, 3); #// LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache)
lRUCache.get(2);    #// returns -1 (not found)
lRUCache.put(4, 4); #// LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    #// return -1 (not found)
lRUCache.get(3);    #// return 3
lRUCache.get(4);    #// return 4 



