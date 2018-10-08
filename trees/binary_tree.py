"""
Implementation for a binary tree.

Includes:
    DFS
        - Preorder traversal
        - Inorder traversal
        - Postorder traversal
    BFS
        - Level order traversal
        - Reverse level order traversal
"""

import sys

sys.path.append("../")


class BinaryNode:
    """A node in a binary tree."""
    
    def __init__(self, data):
        self.value = data
        self.left_child = None
        self.right_child = None

    def set_left(self, data):
        self.left_child = BinaryNode(data)

    def set_right(self, data):
        self.right_child = BinaryNode(data)

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

    def show_all(self):
        print("    ", self.value)
        print("   /", " ", "\ ")
        print(" ", self.left_child.value, "   ", self.right_child.value)

    def __repr__(self):
        return "<Node: {}>".format(self.value)


class BinaryTree:
    """A binary tree data structure."""

    def __init__(self, root):
        self.root = root

    def traverse(self, traversal_type):
        """Traverse the tree in the specified style."""
        if traversal_type == "preorder":
            print(self.preorder_recursive(self.root, "").rstrip("--"))
        elif traversal_type == "inorder":
            print(self.inorder_recursive(self.root, "").rstrip("--"))
        elif traversal_type == "postorder":
            print(self.postorder_recursive(self.root, "").rstrip("--"))                              

    def preorder_recursive(self, start, path):
        """Root --> Left --> Right"""
        if start:
            path += (str(start.value) + "--")
            path = self.preorder_recursive(start.left_child, path)
            path = self.preorder_recursive(start.right_child, path)
        return path

    def inorder_recursive(self, start, path):
        """Left --> Root --> Right"""
        if start:
            path = self.inorder_recursive(start.left_child, path)
            path += (str(start.value) + "--")
            path = self.inorder_recursive(start.right_child, path)
        return path

    def postorder_recursive(self, start, path):
        """Left --> Right --> Root"""
        if start:
            path = self.postorder_recursive(start.left_child, path)
            path = self.postorder_recursive(start.right_child, path)
            path += (str(start.value) + "--")
        return path


"""
Sample binary tree:

          a
       /     \
      b       c
     / \     / \
    d   e   f   g
   /
  h

"""
if __name__ == '__main__':
    # set up tree
    na = BinaryNode("a")
    na.set_left("b")
    na.set_right("c")
    na.get_left().set_left("d")
    na.get_left().set_right("e")
    na.get_right().set_left("f")
    na.get_right().set_right("g")
    na.get_left().get_left().set_left("h")

    bt = BinaryTree(na)
    bt.traverse("postorder")
