def findClosestValueInBst(tree, target):
    # Write your code here.
    # Time Complexity: O(log N)
    # Space Complexity: O(1)
    closet_node = None
    min_diff = float('inf')
    
    while tree != None:
        current_diff = abs(tree.value - target)
        if current_diff < min_diff:
            min_diff = current_diff
            closest_node = tree
            
        if target < tree.value:
            tree = tree.left
        else:
            tree = tree.right

    return closest_node.value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
