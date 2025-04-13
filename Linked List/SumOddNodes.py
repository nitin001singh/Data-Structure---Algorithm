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
        
    def sum_odd_node(self):
        temp = self.head
        counter = 0
        totalSum = 0
        while temp:
            if counter % 2 != 0:
                totalSum += temp.data
            counter += 1
            temp = temp.next
            
        return totalSum
                
                
        
    
l = LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.append(60)
print(l)
output = l.sum_odd_node()
print(output)