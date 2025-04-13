from Node import Node

class LinkedList:
    def __init__(self):    
        self.head = None
        self.size = 0
        
    def __str__(self):
        curr = self.head
        result = ""
        while curr:
            result = result + str(curr.data)
            curr = curr.next
        return result
    
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
        
    def change_sentence(self):
        curr = self.head
        while curr:
            if curr.data == "/" or curr.data == "*":
                curr.data = " "
                
                if curr.next.data == "*" or curr.next.data == "/":
                    curr.next.next.data = curr.next.next.data.upper()
                    curr.next = curr.next.next
                
            curr = curr.next
                

l = LinkedList()
l.append('T')
l.append('h')
l.append('e')
l.append('/')
l.append('*')
l.append('s')
l.append('k')
l.append('y')
l.append('*')
l.append('i')
l.append('s')
l.append('/')
l.append('*')
l.append('b')
l.append('l')
l.append('u')
l.append('e')

print(l)
l.change_sentence()
print(l)