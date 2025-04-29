from collections import defaultdict
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        
    def append(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    
    def remove(self, node):
        node.prev.next =  node.next
        node.next.prev = node.prev
        
    def popTail(self):
        if self.head.next == self.tail:
            return None
        
        tail_node = self.tail.prev
        self.remove(tail_node)
        return tail_node
    
    def isEmpty(self):
        return self.head.next == self.tail
    
    
    
class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.keyTable = {}
        self.freqTable = defaultdict(DoublyLinkedList)
        
        
    def updateFreq(self, node):
        freq = node.freq
        self.freqTable[freq].remove(node)
        if self.freqTable[freq].isEmpty():
            if freq == self.min_freq:
                self.min_freq += 1
            del self.freqTable[freq]
        node.freq += 1
        self.freqTable[node.freq].append(node)
    
    def get(self, key):
        if key not in self.keyTable:
            return None
        else:
            node = self.keyTable[key]
            self.updateFreq(node)
            return node.value
        
    def put(self, key, value):
        if self.capacity == 0:
            return None
        
        if key in self.keyTable:
            node = self.keyTable[key]
            node.value = value
            self.updateFreq(node)

        else:
            if len(self.keyTable) >= self.capacity:
                node = self.freqTable[self.min_freq].popTail()
                if node:
                    del self.keyTable[node.key]
            
            node = Node(key, value)
            self.freqTable[1].append(node)
            self.keyTable[key] = node
            self.min_freq = 1
                
            
            
lfu = LFUCache(2)
lfu.put(1, 10)
lfu.put(2, 20)
print(lfu.get(1))   # 10
lfu.put(3, 30)      # Evicts key 2
print(lfu.get(2))   # -1
print(lfu.get(3))   # 30