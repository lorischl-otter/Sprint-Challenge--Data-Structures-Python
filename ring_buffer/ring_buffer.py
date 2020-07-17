class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # Begin appending index at 0
        self.ind = 0
        # Create empty list to store items
        self.items = []

    def append(self, item):
        # First check if index needs to be reset to not exceed capacity
        if self.ind >= self.capacity:
            self.ind = 0
        # If list is not yet full, append item to end of list
        if len(self.items) < self.capacity:
            self.items.append(item)
        # If list is full, pop item at the given index & replace with new item
        else:
            # Remove current item at given index
            self.items.pop(self.ind)
            # Insert item at given index
            self.items.insert(self.ind, item)
            # Update index
            self.ind += 1

    def get(self):
        # Return list of items
        return self.items
