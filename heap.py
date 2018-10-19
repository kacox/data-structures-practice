"""
Implementation of a Heap data structure.

From Wikipedia:
    '...a heap is a specialized tree-based data structure that satisfies
    the heap property: if P is a parent node of C, then the key (the value)
    of P is either greater than or equal to (in a max heap) or less than or
    equal to (in a min heap) the key of C. The node at the "top" of the
    heap (with no parents) is called the root node.'

    'A common implementation of a heap is the binary heap, in which the
    tree is a binary tree.'

    'A heap is a useful data structure when you need to remove the object
    with the highest (or lowest) priority.'

    'The heap is one maximally efficient implementation of an abstract data
    type called a priority queue...'

Although conceptually heaps are thought of as tree-like, they are best
implemented as arrays (more compact compared to using a Node class).
"""

class MinHeap:
    """Implementation of a Min Heap."""

    def __init__(self):
        self.heap = []

    def insert(self, data):
        pass

    def extract(self):
        pass

    def heapify_up(self):
        pass

    def heapify_down(self):
        pass

    def peek(self):
        pass

    def __repr__(self):
        ans = "< "
        for element in self.heap:
            ans += str(element)
            ans += ", "
        ans = ans.rstrip(", ")
        return ans + " >"