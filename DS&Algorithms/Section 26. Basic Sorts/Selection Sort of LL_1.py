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
        
        # length = n
        # 1st iteration
        # - node to be changed: 1st node (self.head)
        # - from 1st node to last node
        # - find the node which has the minimum value
        # -> switch values between 1st node and min-value node
        # => sorted node: ~ 1st node
        # 2nd iteration
        # - node to be changed: 2nd node
        # - from 2nd node to last node
        # - find the node which has the minimum value
        # -> switch values between 2nd node and min-value node
        # => sorted node: ~ 2nd node
        
        # outer loop: n-1 iterations
        # -> suppose the index of outer loop = i (0 ~ n-2)
        # -> i should be the start index while finding the min-value node
        # inner loop: from start_node to final_node
        str_node = self.head
        for i in range(self.length - 1):
            min_node = str_node
            next_node = str_node.next
            while next_node != None:
                if next_node.value < min_node.value:
                    min_node = next_node
                next_node = next_node.next
            str_node.value, min_node.value = min_node.value, str_node.value
            str_node = str_node.next
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

