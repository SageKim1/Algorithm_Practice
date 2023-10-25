# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space
# n: the number of nodes in the linked list
def middleNode(linkedList):
    # Write your code here.
    slowNode = linkedList
    fastNode = linkedList

    while fastNode and fastNode.next:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    return slowNode
