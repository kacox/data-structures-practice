"""
An implentation of a Queue data structure.

DO NOT IMPLEMENT WITH A LIST (inefficient, use your singly linked list class :D)

Desired operations:
    
    Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
    
    enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
    
    dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
    
    isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
    
    size() returns the number of items in the queue. It needs no parameters and returns an integer.

"""

import singly_linked_list as ll


class Queue:
    """A queue data structure."""

    def __init__(self):
        self.members = ll.LinkedList()

    def enqueue(self, item):
        self.members.append(item)

    def dequeue(self):
        self.members.pop()

    def is_empty(self):
        return self.members.is_empty()

    def get_size(self):
        return self.members.get_size()

    def __repr__(self):
        repr_str = "[Queue: "

        if self.members.head:
            current = self.members.head
            while current.next:
                repr_str = repr_str + str(current) + ", "
                current = current.next
            repr_str = repr_str + str(current)

        return repr_str + "]"


if __name__ == '__main__':
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    q.enqueue("d")