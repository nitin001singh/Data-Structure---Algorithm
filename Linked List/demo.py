class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
        
        
class LinkedList:
    
    def __init__(self):
        self.head=  None
        
        
    def __str__(self):
        
        result = ""
        current = self.head
        while current:
            result += str(current.data) + " => "
            current = current.next
        
        result = result[:-4]
        
        return result
            
        
        
    def insertAtHead(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
            
        return self.head
             
    def insertAtPos(self, pos, value):
        node = Node(value)
        current = self.head
        i = 1
        while current:
            if i == pos:
                node.next = current.next
                current.next = node
                return
            i += 1            
            current= current.next
        
        return self.head
    

l = LinkedList()
l.insertAtHead(5)
l.insertAtHead(10)
l.insertAtHead(15)
l.insertAtHead(20)
print(l)
l.insertAtPos(30,1)

print(l)