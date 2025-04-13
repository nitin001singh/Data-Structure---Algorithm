from Node import Node

class LinkedList:
    def __init__(self):    
        self.head = None
        self.size = 0
        
    def __str__(self):
        curr = self.head
        result = ""
        while curr:
            result = result + str(curr.data) + " => "
            curr = curr.next
        return result[:-4]
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.size += 1
            return
        
        
        curr = self.head
        while curr.next:
            curr = curr.next
            
        curr.next = new_node
        self.size += 1
        
    def replace_max(self, value):
        temp = self.head
        max = temp
        while temp:
            if temp.data > max.data:
                max = temp
            temp = temp.next
        max.data = value
        
    
l = LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l)
l.replace_max(100)
print(l)