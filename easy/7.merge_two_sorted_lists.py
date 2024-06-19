# list1 = []
# list2 = [0]

# list3 =sorted(list1 + list2)
# print(list3)


class node:
    def __init__(self, data=None) -> None:
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self) -> None:
        self.head = node()

    def append(self, data):
        current = self.head

        while current.next != None:
            current = current.next
        
        current.next = node(data)
        # print(current.data)
        # print(current.next.data)
        # print(current.next.next)


    def display_list(self):

        current = self.head
        gathered_list = []

        while current.next != None:
            # print(current.data)
            # print(current.next.data)
            current = current.next 
            gathered_list.append(current.data)

        return gathered_list


l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l2 = LinkedList()
l2.append(1)
l2.append(2)
l2.append(4)
l2.append(5)
# data = l1.display_list()
# print(data)

# print(l1.head.next.next.data)

def merge_two_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:

    dummy = LinkedList()

    tail = dummy

    l1 = l1.head.next
    l2 = l2.head.next

    while l1 and l2:
        print(l1.data, l2.data)

        if l1.data < l2.data:
            dummy.append(l1.data)
            l1 = l1.next
        else:
            dummy.append(l2.data)
            # tail.next = l2
            l2 = l2.next
    while l1 or l2:
        if l1:
            dummy.append(l1.data)
            l1 = l1.next
        if l2:
            dummy.append(l2.data)
            l2=l2.next
        # tail = tail.next

    

    return dummy.display_list()

print(merge_two_lists(l1, l2))

            
