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

    # WRITE SELECTION_SORT METHOD HERE #
    def selection_sort(self):
        if self.length < 2:
            return
        
        # start from the first node (to find the min-value node)
        # the node which will be switched with the min-value node
        current = self.head
        # until the last node (last_node.next == None)
        while current.next is not None:
            # init the smallest node
            smallest = current
            # next nodes which will be compared with min-value node
            inner_current = current.next
            while inner_current is not None: # until the last node
                if inner_current.value < smallest.value:
                    smallest = inner_current # update min-value node
                inner_current = inner_current.next
            # deals with edge case: current node = min-value node
            if smallest != current:
                current.value, smallest.value = smallest.value, current.value
            current = current.next
        #self.tail = current
    ####################################



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""
