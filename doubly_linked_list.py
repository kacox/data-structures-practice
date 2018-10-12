"""Implementation for a Doubly Linked List data structure."""

class Node:
    """A node in a DLL."""

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __repr__(self):
        return "<Node: {}>".format(self.data)

class DoublyLinkedList:
    """A Doubly Linked List (DLL)."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        """Add a node to the end of the DLL."""
        if not self.head:
            first_node = Node(data)
            self.head = first_node
            self.tail = first_node
        else:
            current = self.head
            while current.next:
                # traverse to the last node
                current = current.next
            current.next = Node(data)
        

    def insert(self, data, new_data):
        """Insert a node before a given node."""
        pass

    def remove(self, data):
        """Remove a node from the DLL."""
        pass

    def __repr__(self):
        """Human readible version of the DLL."""
        if self.head:
            ans = str(self.head.data)
            current = self.head
            while current.next:
                ans = " <--> ".join([ans, str(current.next.data)])
                current = current.next
            return "[" + ans + "]"
        else:
            return "Empty DLL"


if __name__ == '__main__':
    # Make and test the DLL
    dll = DoublyLinkedList()
    dll.add(6)
    dll.add(2)
    dll.add(12)
    dll.add(9)
    dll.add(22)