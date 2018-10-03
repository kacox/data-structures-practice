"""
Implementation for a SINGLY linked list.
"""


class Node():
    """Represents a node in a SINGLY linked list."""
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def __repr__(self):
        return "<Node: {}>".format(self.data)


class LinkedList():
    """Represents a SINGLY linked list."""
    
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        """Adds a new data to the end of the list."""
        if not self.head:
            self.head = Node(data)
            self.size += 1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            self.size += 1

    def remove(self, data):
        """Removes a Node from the list."""
        if self.is_empty():
            return "The list is empty."
        
        current = self.head
        previous = None
        found = False

        while not found:
            if current.data is data:
                found = True
            elif not current.next:
                break
            else:
                previous = current
                current = current.next

        if not found:
            return "This node is not in the linked list."

        if previous is None:
            # beginning
            self.head = current.next
            current.next = None
            self.size -= 1
        elif not current.next:
            # end
            previous.next = None
            self.size -= 1
        else:
            # middle
            previous.next = current.next
            current.next = None
            self.size -= 1

    def search(self, data):
        """
        Searches for the existence of a Node in the list. Returns a 
        boolean value.
        """
        if self.is_empty():
            return False

        current = self.head
        while current.next:
            if current.data == data:
                return True
            current = current.next

        if current.data == data:
                return True
        return False

    def is_empty(self):
        """Determines if the list is empty. Returns a boolean."""
        return self.head == None

    def get_size(self):
        """Returns the size of the list as an integer."""
        return self.size

    def get_index(self, data):
        """
        Returns the position (index) of an node in the list. Takes
        data and returns the index."""
        if self.is_empty():
            return "The list is empty."

        if self.head.data == data:
            return 0
        else:
            if self.get_size() < 2:
                return "This node is not in the list."

            current = self.head
            indx = 0
            while current.next:
                current = current.next
                indx += 1

                if current.data == data:
                    return indx

            return "This node is not in the list."

    def insert(self, pos, data):
        """
        Adds a new Node to the list at position pos. Takes pos and
        data; returns nothing.
        """
        if self.is_empty():
            if pos == 0:
                self.append(data)
                return
        elif pos == self.size:
            self.append(data)
            return
        if pos > self.size:
            print("Out of range.")
            return

        current = self.head
        previous = None
        indx = 0

        if pos == 0:
            self.head = Node(data)
            self.head.next = current
            self.size += 1
            return

        while current.next:
            previous = current
            current = current.next
            indx += 1
            if pos == indx:
                previous.next = Node(data)
                previous.next.next = current
                self.size += 1            

        return None

    def pop(self, pos=None):
        """
        Removes and returns a Node from the list.
        
        By default, removes the last Node from the list. If pos given,
        removes and returns the item at position pos.
        """
        if pos is None:
            pos = self.size - 1

        if self.is_empty():
            return "The list is empty."
        
        current = self.head
        indx = 0
        previous = None
        found = False

        while not found:
            if indx == pos:
                found = True
            elif not current.next:
                break
            else:
                previous = current
                current = current.next
                indx += 1

        if not found:
            return "This node is not in the linked list."

        if previous is None:
            # beginning
            self.head = current.next
            current.next = None
            self.size -= 1
            return current
        elif not current.next:
            # end
            previous.next = None
            self.size -= 1
            return current
        else:
            # middle
            previous.next = current.next
            current.next = None
            self.size -= 1
            return current

    def reverse(self):
        """Reverse the linked list. Returns nothing."""
        previous = None
        current = self.head
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        self.head = previous

    def __repr__(self):
        repr_head = "[Linked List -- size: {}".format(self.size)

        tail = " -- Members: "
        if self.head:
            current = self.head
            while current.next:
                tail = tail + str(current) + ", "
                current = current.next
            tail = tail + str(current)
            return repr_head + tail + "]"
        else:
            return repr_head + "]"


################################################################
if __name__ == "__main__":
    ll = LinkedList()
    for werd in ["this", "is", "fun"]:
        ll.append(werd)

    print(ll, "\n")
