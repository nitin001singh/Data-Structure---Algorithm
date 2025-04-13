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
        
    def reverse_linked_list(self):
        curr = self.head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        self.head = prev
            
            
            
        
    
l = LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.append(60)
print(l)
l.reverse_linked_list()
print(l)