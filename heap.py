"""
Implementation of Heap data structures.

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

    Tree:
          8
        /   \
       10    20
      /  \
    17    15

    Array:
    [8, 10, 20, 17, 15]

    How to map parent/children indices:
    parent = (left_child_index - 1) / 2
    parent = (right_child_index - 2) / 2
    left = (index_of_parent * 2) + 1
    right = (index_of_parent * 2) + 2
"""

class MinHeap:
    """Implementation of a binary Min Heap."""

    def __init__(self):
        self.heap = [10, 15, 20, 17]

    def insert(self, data):
        """
        Insert the new element at the bottom of the heap (end of the
        array / the bottom left unoccupied spot that maintains balance)
        then heapify up until in the correct position.
        """
        # add to the bottom of the heap
        self.heap.append(data)

        # move up to correct position
        self.heapify_up()

    def extract(self):
        """
        Remove the minimum value from the top of the heap, then heapify
        down until heap property restored.
        """
        if self.heap:
            # remove min val from top, set new top value (swap and pop)
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            min_item = self.heap.pop()

            # find correct spot for new top of heap
            self.heapify_down()

            # return the removed min value
            return min_item

    def heapify_up(self):
        """
        Move the most recently added element up the heap into its correct
        position.
        """

        # in response to insert
        # start at last position (most recently added); "bottom" of the heap
        # walk up as long as there is a parent element ("bubble up")
        # and the item is out of order (compare to parent)
        # in min heap, swap if parent less than current
            # (their indices would swap since in a list?)

        if len(self.heap) > 1:
            current_index = len(self.heap) - 1
            parent_index = self.get_parent_index(current_index)

            while (self.has_parent(current_index) and
                    self.heap[current_index] < self.heap[parent_index]):
                # swap
                self.swap(current_index, parent_index)
                # walk up
                current_index = self.get_parent_index(current_index)


    def heapify_down(self):
        """
        In response to extraction, put the most recently added item at the
        top of the heap, then move it downwards until in the correct
        position.
        """

        # start at root
        current_index = 0
        # while a left child exists, walk downwards ("bubble down")
        while self.has_left_child(current_index):
            # aside: if no left child, no right child can exist (insertion rules prevent)
            # assume left child has smaller value
            smaller_child_index = self.get_left_child_index(current_index)
            # then check if right child exists, if so see if its value smaller
            if self.has_right_child(current_index) and (self.heap[self.get_right_child_index(current_index)] < self.heap[smaller_child_index]):
                # if so, set as the smaller child index (instead of left child)
                smaller_child_index = self.get_right_child_index(current_index)

            # check if in order, exit while loop
            if self.heap[current_index] < self.heap[smaller_child_index]:
                break
            # else, swap value with smaller child
            else:
                self.swap(current_index, smaller_child_index)

            # move down to smaller child
            current_index = smaller_child_index

    def peek(self):
        """Show the top item in the heap."""
        if self.heap:
            return self.heap[0]

    """Helper methods for heapify methods."""
    def swap(self, first_index, second_index):
        """Swap two items in the heap."""
        self.heap[first_index], self.heap[second_index] = self.heap[second_index], self.heap[first_index]

    def get_left_child_index(self, parent_index):
        """Get the index of the left child."""
        # b/c a binary min heap, can calculate correct location
        return (2 * parent_index) + 1

    def get_right_child_index(self, parent_index):
        """Get the index of the left child."""
        # b/c a binary min heap, can calculate correct location
        return (2 * parent_index) + 2

    def get_parent_index(self, child_index):
        """Get index of parent.

        # TODO: only works for right children (see original mapping
                comments at beginning of file; also below). Left
                children are unable to find the correct parent.

                Try with h.insert(14) then h.insert(9) to demo the
                problem.

                How to map to parent indices:
                    parent = (left_child_index - 1) // 2
                    parent = (right_child_index - 2) // 2
        """
        return (child_index - 2) // 2

    def has_left_child(self, parent_index):
        """Indicates if a left child exists."""
        return self.get_left_child_index(parent_index) < len(self.heap)

    def has_right_child(self, parent_index):
        """Indicates if a right child exists."""
        return self.get_right_child_index(parent_index) < len(self.heap)

    def has_parent(self, child_index):
        return self.get_parent_index(child_index) >= 0

    def __repr__(self):
        ans = "< "
        for element in self.heap:
            ans += str(element)
            ans += ", "
        ans = ans.rstrip(", ")
        return ans + " >"


if __name__ == '__main__':
    h = MinHeap()