class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target equals root value, return true
        if target == self.value:
            return True
        # else, check value of target to follow right or left nodes
        else:
            # mimic structure of insert to find where value would be
            if target < self.value:
                # if target is less than parent,
                # but left node is empty, return False
                if self.left is None:
                    return False
                # otherwise, continue recursively w/ left node
                else:
                    return self.left.contains(target)
            # if target is larger than root/parent, go to right node
            else:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
