# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log N) time | O(log N) space
    # Worst: O(n) time | O(n) space
    def insert(self, value):
        # Write your code here.
        if value < self.value:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        # Do not edit the return statement of this method.
        return self

    # Average: O(log N) time | O(log N) space
    # Worst: O(n) time | O(n) space
    def contains(self, value):
        # Write your code here.
        if value < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    # Average: O(log N) time | O(log N) space
    # Worst: O(n) time | O(n) space
    def remove(self, value, parent=None):
        # Write your code here.
        if value < self.value:
            if self.left != None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right != None:
                self.right.remove(value, self)
        else:
            if self.left != None and self.right != None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parent == None:
                if self.left != None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right != None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left != None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left != None else self.right
        # Do not edit the return statement of this method.
        return self

    def getMinValue(self):
        if self.left == None:
            return self.value
        else:
            return self.left.getMinValue()
