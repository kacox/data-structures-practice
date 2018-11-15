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

    def add_node(self, node):
        """Add a Node to the graph."""
        self.nodes[node.key] = node
        self.size += 1

    def make_edge(self, start, end):
        """Make an undirected edge between two nodes."""
        if start not in self.nodes:
            start_node = Node(start)
            self.add_node(start_node)
        elif start in self.nodes:
            start_node = self.nodes[start]

        if end not in self.nodes:
            end_node = Node(end)
            self.add_node(end_node)
        elif end in self.nodes:
            end_node = self.nodes[end]

        start_node.add_neighbor(end_node)
        end_node.add_neighbor(start_node)

    def get_node(self, key):
        """Returns a Node object from the graph."""
        if key in self.nodes:
            return self.nodes[key]
        return None

    def get_nodes(self):
        """Returns a list of Node objects in the graph."""
        return list(self.nodes.values())

    def bfs(self, start):
        """Breadth-first search from given start key."""
        if start in self.nodes:
            path = []

            # using a list for ease; not as efficient as dll
            q = []
            seen = set([])

            q.append(self.nodes[start])
            seen.add(start)

            while q:
                current = q.pop(0)
                path.append(current.key)
                for neighbor in current.neighbors:
                    if neighbor.key not in seen:
                        q.append(neighbor)
                        seen.add(neighbor.key)
            return path

        else:
            print("This starting node is not in the graph.")

    def dfs(self):
        pass

    def __contains__(self, key):
        """Graph membership testing."""
        return key in self.nodes

    def __repr__(self):
        """Display contents of the graph."""
        contents = []
        for node_key in self.nodes.keys():
            contents.append(str(node_key))
        return "{" + ", ".join(contents).rstrip(", ") + "}"


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
    # print(graph, "\n")
    # print(graph.nodes)
