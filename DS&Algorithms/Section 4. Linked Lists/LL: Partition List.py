class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    # WRITE PARTITION_LIST METHOD HERE #
    def partition_list(self, value):
        if not self.head:
            return None
            
        dummy_s = Node(0)
        dummy_b = Node(0)
        prev_s = dummy_s
        prev_b = dummy_b
        
        current = self.head
        while current:
            if current.value < value:
                prev_s.next = current
                prev_s = prev_s.next
            else:
                prev_b.next = current
                prev_b = prev_b.next
            current = current.next
        
        prev_s.next = None
        self.tail = prev_b
        prev_b.next = None
        prev_s.next = dummy_b.next
        
        self.head = dummy_s.next
    ####################################
    
    

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10


"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""
