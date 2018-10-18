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

import doubly_linked_list as dll


class Deque:
    """f"""

    def __init__(self):
        self.size = 0
        self.items = dll.DoublyLinkedList()

    def add_front(self, item):
        """Add an item to the front of the deque."""
        self.items.insert(0, item)
        self.size += 1

    def add_rear(self, item):
        """Add an item to the rear of the deque."""
        self.items.append(item)
        self.size += 1

    def remove_front(self):
        """Remove an item from the front of the deque."""
        self.size -= 1
        return self.items.remove(self.items.head.data)

    def remove_rear(self):
        """Remove an item from the rear of the deque."""
        self.size -= 1
        return self.items.pop()

    def is_empty(self):
        """Check if the deque is empty."""
        return self.size == 0

    def get_size(self):
        """Return the size of the deque."""
        return self.size

    def __repr__(self):
        return self.items.__repr__()


if __name__ == '__main__':
    d = Deque()
    d.add_front("a")
    d.add_front("b")
    d.add_rear("c")
    print(d)