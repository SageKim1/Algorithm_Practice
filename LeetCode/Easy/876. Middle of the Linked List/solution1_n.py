class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    def find_middle_node(self):
        pt1 = pt2 = self.head
        while pt2 is not None and pt2.next is not None:
            pt1 = pt1.next
            pt2 = pt2.next.next
        return pt1
    ######################################




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""
