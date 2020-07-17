import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

'''
Written response:
The runtime complexity of the initial solution is O(n^2), or quadratic time,
and ran on my computer in 13.22 seconds.
'''

# Instantiate bstnode for first list of names
bst1 = BSTNode(names_1[0])

# Insert list of names into bst1
for name in names_1:
    bst1.insert(name)

# Check for duplicates from names_2
for name in names_2:
    if bst1.contains(name):
        duplicates.append(name)


'''
Given that  this solution implements a binary search tree,
the runtime complexity for the improved implementation is O(log n).
This solution ran on my computer in .16 seconds.
'''


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"BST runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this
# problem. What's the best time you can accomplish?  There are no restrictions
# on techniques or data structures, but you may not import any additional
# libraries that you did not write yourself.

# Start time
start_time = time.time()

# Read files
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Try built-in Python approach with set equivalence
duplicates_2 = list(set(names_1) & set(names_2))

# Also tried using set intersection, but time was roughly equivalent
# and sometimes a hair longer, and also requires more characters
# duplicates_2 = list(set(names_1).intersection(set(names_2)))

# End time and print results
end_time = time.time()
print(f"{len(duplicates_2)} duplicates:\n\n{', '.join(duplicates_2)}\n\n")
print(f"Python runtime: {end_time - start_time} seconds")

print(f"\nConfirm lists are equal: {set(duplicates) == set(duplicates_2)}\n")

'''
This Python set implementation ran in .004 seconds on my computer!
'''
