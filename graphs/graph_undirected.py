"""
Implementation for an undirected, unweighted graph data structure.
"""

class Node:
    """Represents a node in an undirected graph."""

    def __init__(self, value):
        self.key = value
        self.neighbors = set([])

    def add_neighbor(self, node):
        self.neighbors.add(node)


class Graph:
    """Represents an undirected, unweighted graph."""

    def __init__(self):
        # so you can easily access a Node from a key
        self.nodes = {}
        self.size = 0

    def add_node(self, key):
        self.nodes[key] = Node(key)
        self.size += 1

    def make_edge(self, start, end):
        """Make an undirected edge between two nodes."""
        if start not in self.nodes:
            self.add_node(start)
        if end not in self.nodes:
            self.add_node(end)
        self.nodes[start].add_neighbor(self.nodes[start])
        self.nodes[end].add_neighbor(self.nodes[end])

    def get_node(self, key):
        """Returns a Node object from the graph."""
        if key in self.nodes:
            return self.nodes[key]
        return None

    def get_nodes(self):
        """Returns a list of Node objects in the graph."""
        return list(self.nodes.values())

    def __contains__(self, key):
        """Graph membership testing."""
        return key in self.nodes


if __name__ == '__main__':
    # build a graph
    #
    #    0 -- 1
    #   /      \ 
    #  4 ------ 2 -- 3 -- 5

    graph = Graph()
    graph.make_edge(0, 1)
    graph.make_edge(2, 1)
    graph.make_edge(2, 4)
    graph.make_edge(0, 4)
    graph.make_edge(2, 3)
    graph.make_edge(3, 5)
    print(graph.nodes)
    print(graph.size)

