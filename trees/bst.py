"""Implementation for Binary Search Tree."""

class BinaryNode:
    """A node in a BST."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return "<Node: {}>".format(self.data)


class BinarySearchTree:
    """A Binary Search Tree."""

    def __init__(self, node):
        """Create a BST with a specified root node."""
        self.root = node

    def insert(self, node):
        """Insert a node into the BST."""
        inserted = False
        current_node = self.root

        while not inserted:
            if node.data > current_node.data:
                if not current_node.right:
                    current_node.right = node
                    inserted = True
                current_node = current_node.right

            elif node.data < current_node.data:
                if not current_node.left:
                    current_node.left = node
                    inserted = True
                current_node = current_node.left

            else:
                print("Something isn't right!!")
                break


    def search(self, data):
        """Search for a node by its data attribute."""
        current_node = self.root
        searching = True

        while searching:
            if data > current_node.data:
                if not current_node.right:
                    return False
                current_node = current_node.right
            elif data < current_node.data:
                if not current_node.left:
                    return False
                current_node = current_node.left
            else:
                return True

    def traverse_inorder(self):
        """InOrder traversal of the BST."""
        traversal = []

        def _traverse_inorder(current_node):
            """InOrder traversal of the BST."""
            if current_node:
                _traverse_inorder(current_node.left)
                traversal.append(current_node.data)
                _traverse_inorder(current_node.right)

        if self.root:
            _traverse_inorder(self.root)
        return traversal

    def __repr__(self):
        return "[ BST, root: {} ]".format(self.root)


###########################################################
if __name__ == '__main__':
    # Make a sample BST
    n10 = BinaryNode(10)
    n9 = BinaryNode(9)
    n15 = BinaryNode(15)
    n21 = BinaryNode(21)
    n2 = BinaryNode(2)
    n50 = BinaryNode(50)

    bst = BinarySearchTree(n10)
    bst.insert(n9)
    bst.insert(n15)
    bst.insert(n21)
    bst.insert(n2)
    bst.insert(n50)

    print(bst.traverse_inorder())
