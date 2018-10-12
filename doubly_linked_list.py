"""Implementation for a Doubly Linked List data structure."""

class Node:
    """A node in a DLL."""

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __repr__(self):
        return "<Previous: {}>--<Node: {}>--<Next: {}>".format(self.previous,
                                                                self.data,
                                                                self.next)

class DoublyLinkedList:
    """A Doubly Linked List (DLL)."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        """Add a node to the DLL."""
        pass

    def insert(self, data, new_data):
        """Insert a node before a given node."""
        pass

    def remove(self, data):
        """Remove a node from the DLL."""
        pass

    def __repr__(self):
        # Traverse the DLL
        pass