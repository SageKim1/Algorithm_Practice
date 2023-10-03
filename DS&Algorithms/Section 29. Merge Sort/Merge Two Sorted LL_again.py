class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE MERGE METHOD HERE #
    def merge(self, other_list):
        dummy = Node(0)
        current = dummy
        
        ori_head = self.head
        other_head = other_list.head
        while ori_head != None and other_head != None:
            if ori_head.value < other_head.value:
                current.next = ori_head
                temp = ori_head.next
                ori_head.next = None
                ori_head = temp
            else:
                current.next = other_head
                temp = other_head.next
                other_head.next = None
                other_head = temp
                
            current = current.next
        
        if ori_head != None:
            current.next = ori_head
        
        if other_head != None:
            current.next = other_head
            self.tail = other_list.tail
        
        self.head = dummy.next
        self.length += other_list.length
    ###########################
    


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""
