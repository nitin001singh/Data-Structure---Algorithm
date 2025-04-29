# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def reverse_in_groups(head, k):
#     dummy = Node(0)
#     dummy.next = head
#     groupPrevious = dummy

#     while True:
#         group_end = groupPrevious
#         for i in range(k):
#             group_end = group_end.next
#             if not group_end:
#                 return dummy.next

#         group_next = group_end.next
#         prev = group_next
#         current = groupPrevious.next

#         for i in range(k):
#             temp = current.next
#             current.next = prev
#             prev = current
#             current = temp


#         temp = groupPrevious.next
#         groupPrevious.next = group_end
#         groupPrevious = temp

#     return dummy.next


# def build_linked_list(values):
#     if not values:
#         return None
#     head = Node(values[0])
#     current = head
#     for val in values[1:]:
#         current.next = Node(val)
#         current = current.next
#     return head

# def print_linked_list(head):
#     while head:
#         print(head.value, end=' -> ' if head.next else '\n')
#         head = head.next



# head = build_linked_list([1, 2, 3, 4, 5, 6, 7, 8,9])
# k = 3
# new_head = reverse_in_groups(head, k)
# print_linked_list(new_head)






class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

    def reverse_in_groups(self, head, k):
        
        if not head  and  not head.next and k == 1:
            return head
        
        
        dummy = Node(0)
        dummy.next = head
        beforeStart = dummy
        end = head
        i = 0

        while end:
            i += 1
            if i % k == 0:
                start = beforeStart.next
                temp = end.next
                self.reverse(start, end)
                start.next = temp
                
                
                
                
            else:
                end = end.next
            

        return dummy.next


    def build_linked_list(values):
        if not values:
            return None
        head = Node(values[0])
        current = head
        for val in values[1:]:
            current.next = Node(val)
            current = current.next
        return head

    def print_linked_list(head):
        while head:
            print(head.value, end=' -> ' if head.next else '\n')
            head = head.next



    head = build_linked_list([1, 2, 3, 4, 5, 6, 7, 8,9])
    k = 3
    new_head = reverse_in_groups(head, k)
    print_linked_list(new_head)
