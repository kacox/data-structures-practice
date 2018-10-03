"""
Implementation of a Stack data structure.
"""


class Stack:
    """A stack data structure."""

    def __init__(self):
        """Creates a new empty stack."""
        self.members = []

    def push(self, *args):
        """Adds new item(s) to the top of the stack. Returns nothing."""
        for item in args:
            self.members.append(item)

    def pop(self):
        """Removes and returns the top item from the stack."""
        return self.members.pop()

    def peek(self):
        """Returns the top item from the stack but does not remove it."""
        return self.members[-1]

    def is_empty(self):
        """Indicates whether or not the stack is empty. Returns a boolean."""
        return len(self.members) == 0

    def size(self):
        """Returns the number of items on the stack. Returns an integer."""
        return len(self.members)

    def __repr__(self):
        """Human-readable representation of the stack."""
        return "bottom --> [" + ", ".join([member for member in self.members]) + "] <-- top"


if __name__ == "__main__":
    stk = Stack()
    stk.push("this")
    stk.push("is", "fun")

    print(stk)