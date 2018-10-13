"""
Double-ended queue implementation using a doubly-linked list.

The deque abstract data type is defined by the following structure and
operations. A deque is structured, as described above, as an ordered
collection of items where items are added and removed from either end,
either front or rear. The deque operations are given below.

    Deque() creates a new deque that is empty. It needs no parameters and
    returns an empty deque.

    addFront(item) adds a new item to the front of the deque. It needs the
    item and returns nothing.

    addRear(item) adds a new item to the rear of the deque. It needs the item
    and returns nothing.

    removeFront() removes the front item from the deque. It needs no
    parameters and returns the item. The deque is modified.

    removeRear() removes the rear item from the deque. It needs no parameters
    and returns the item. The deque is modified.

    isEmpty() tests to see whether the deque is empty. It needs no parameters
    and returns a boolean value.

    size() returns the number of items in the deque. It needs no parameters
    and returns an integer.

*Definition of and method signatures are from "Problem Solving with
Algorithms and Data Structures using Python" by Brad Miller and David Ranum,
Luther College
"""


class Deque:
    """f"""

    def __init__(self):
        self.size = 0
        self.items = None # TODO: make a doubly-linked list to store items

    def add_front(self, item):
        """Add an item to the front of the deque."""
        pass

    def add_rear(self, item):
        """Add an item to the rear of the deque."""
        pass

    def remove_front(self):
        """Remove an item from the front of the deque."""
        pass

    def remove_rear(self):
        """Remove an item from the rear of the deque."""
        pass

    def is_empty(self):
        """Check if the deque is empty."""
        return self.size() == 0

    def size(self):
        """Return the size of the deque."""
        return self.size()