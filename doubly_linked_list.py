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
        self.size = 0

    def append(self, data):
        """Append a node to the end of the DLL."""
        if not self.head:
            first_node = Node(data)
            self.head = first_node
            self.tail = first_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            current.next.previous = current
            self.tail = current.next
        self.size += 1

    def insert_after(self, data, new_data):
        """Insert a node after a given node."""
        if self.head:
            # traverse until data is found or until the end of the dll
            # if data is found, insert new_data after it (data.next), then return
            # if end of dll is reached, without finding, do nothing (message)
            if self.head.data == data:
                # beginning insert
                new_data_next = self.head.next
                self.head.next = Node(new_data)
                self.head.next.previous = self.head
                self.head.next.next = new_data_next
                self.size += 1
                if self.size == 2:
                    self.tail = self.head.next

            # middle insert

            # end insert


    def remove(self, data):
        """Remove a node from the DLL."""
        pass

    def pop(self):
        """Remove a node from the end of the DLL."""
        if self.head:
            current = self.head
            while current.next:
                current = current.next

            if current.previous:
                # not the head
                current.previous.next = None
                current.previous = None
            else:
                self.head = None
                self.tail = None

            self.size -= 1

    def search(self, data):
        """Determine the existence of a node in the DLL."""
        pass

    def is_empty(self):
        """Returns whether or not the DLL is empty."""
        return self.get_size() == 0

    def get_size(self):
        """Returns the size of the DLL."""
        return self.size

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
    dll.append(6)
    dll.append(2)
    dll.append(12)
    dll.append(9)
    dll.append(22)