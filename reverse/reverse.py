class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # Recursive solution to reverse list
        # Base case is either an empty list or reaching the end of the list
        if node is None:
            return self
        else:
            # Set head to current node
            self.head = node
            # Create a pointer for next node
            nn = node.next_node
            # Reset next node to previous node
            node.set_next(prev)
            # Repeat function
            return(self.reverse_list(nn, node))
