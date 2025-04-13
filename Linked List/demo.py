class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        curr = self.head
        result = ""
        while curr:
            result += str(curr.data) + " => "
            curr = curr.next
        return result[:-4] if result else ""

    def __len__(self):
        return self.size

    def insertHead(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def insertTail(self, value):
        if self.size == 0:
            self.insertHead(value)
            return
        node = Node(value)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        self.size += 1

    def insertAtPosition(self, position, value):
        if position < 0 or position > self.size:
            raise IndexError("Invalid index")

        if position == 0:
            self.insertHead(value)
            return

        node = Node(value)
        curr = self.head
        pos = 0
        while curr:
            if pos == position - 1:
                node.next = curr.next
                curr.next = node
                self.size += 1
                return
            curr = curr.next
            pos += 1

    def removeHead(self):
        if self.size == 0:
            raise IndexError("List is empty")
        self.head = self.head.next
        self.size -= 1

    def clear(self):
        if self.size == 0:
            raise IndexError("List is already empty")
        self.head = None
        self.size = 0

    def removeLast(self):
        if self.size == 0:
            raise IndexError("List is already empty")
        elif self.size == 1:
            self.removeHead()
            return

        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None
        self.size -= 1

    def removeAt(self, position):
        if position < 0 or position >= self.size:
            raise IndexError("Invalid index")

        if position == 0:
            self.removeHead()
            return

        curr = self.head
        pos = 0
        while curr:
            if pos == position - 1:
                curr.next = curr.next.next
                self.size -= 1
                return
            curr = curr.next
            pos += 1

    def search(self, item):
        curr = self.head
        pos = 0
        while curr:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1
        raise ValueError("Item not found")

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")

        curr = self.head
        pos = 0
        while curr:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
            
    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        self.head = prev
            


# Test cases
if __name__ == "__main__":
    l = LinkedList()

    l.insertHead(5)
    l.insertHead(6)
    l.insertHead(7)
    l.insertHead(8)            # 8 => 7 => 6 => 5
    l.insertTail(80)          # 8 => 7 => 6 => 5 => 80
    l.insertAtPosition(4, 50) # 8 => 7 => 6 => 5 => 50 => 80
    
    print(l)
    l.reverse()
    print(l)
    