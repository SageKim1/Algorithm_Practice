class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()




#### WRITE SORT_STACK FUNCTION HERE #####
#                                       #
#  This is a separate function that is  #
#  not a method within the Stack class. #
#  Indent all the way to the left.      #
#                                       #
def sort_stack(ascending_stack):
    descending_stack = Stack()
    
    while not ascending_stack.is_empty():
        temp = ascending_stack.pop()
        
        while not descending_stack.is_empty() \
        and descending_stack.peek() > temp:
            ascending_stack.push(descending_stack.pop())
        
        descending_stack.push(temp)
    
    while not descending_stack.is_empty():
        ascending_stack.push(descending_stack.pop())
#########################################




my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
