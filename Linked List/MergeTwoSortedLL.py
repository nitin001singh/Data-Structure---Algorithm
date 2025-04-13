# Optimal 

# TC : O(N)
# Sc : O(1)


from Node import Node
from LinkedList import LinkedList
           
    
l1 = LinkedList()
l1.append(1)
l1.append(3)
l1.append(5)
l1.append(9)

l2 = LinkedList()
l2.append(2)
l2.append(6)
l2.append(4)
l2.append(7)


def mergeLL(l1, l2):
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    return dummy.next


merged_head = mergeLL(l1.head, l2.head)

while merged_head:
    print(merged_head.data, end=" => ")
    merged_head = merged_head.next
print("None")