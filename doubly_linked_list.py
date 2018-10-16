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

    def insert(self, pos, data):
        """Insert a node at a given position (pushes old node forward)."""
        if pos > self.size:
            print("Position out of range.")
            return

        if not self.head and pos == 0:
            # insert as first node in DLL
            self.append(data)

        elif self.head:
            current_pos = 0
            new_node = Node(data)

            # insert at beginning (of non-empty list)
            if pos == 0:
                self.head.previous = new_node
                new_node.next = self.head
                self.head = new_node
                self.size += 1
                return

            # middle insert
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
                current_pos += 1

                if current_pos == pos:
                    current_node.previous.next = new_node
                    new_node.next = current_node
                    new_node.previous = current_node.previous
                    current_node.previous = new_node
                    self.size += 1
                    return

            # insert at end
            self.append(data)

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
    # dll.append(9)
    # dll.append(22)