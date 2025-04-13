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
        
    def remove_duplicates(self):
        temp = self.head
        while temp and temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return self.head
            
      
                
        
    
l = LinkedList()
l.append(1)
l.append(1)
l.append(2)
l.append(2)
l.append(3)
l.append(3)
print(l)
output = l.remove_duplicates()

while output:
    print(output.data, end=" => ")
    output = output.next