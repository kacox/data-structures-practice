"""
Implementation for an undirected, weighted graph data structure. Very
similar to `graph_undirected.py` implementation.


     (0)---7---(1)
    /            \
   1              2
  /                \ 
(4)-------4--------(2)----3----(3)---2---(5)
"""

import random

# adjacency list representation of above graph
# { nodeA: {neighbor: edge_weight, neighbor: edge_weight}, 
#   nodeB: {neighbor: edge_weight},
#   ...,
#   nodeN: {neighbor: edge_weight, ...}
# }
graph = {0: {1: 7, 4: 1},
            1: {0: 7, 2: 2},
            2: {1: 2, 4: 4, 3: 3},
            3: {2: 3, 5: 2},
            4: {2: 4, 0: 1},
            5: {3: 2}}


# use to test that the graph was created appropriately
def dfs(graph):
    if graph:
        stack = []
        visited = set()

        start = random.choice(list(graph.keys()))
        stack.append(start)
        visited.add(start)
        while stack:
            current_node = stack.pop() 
            print(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)


def find_shortest_paths(graph, source_node):
    """
    Find the shortest paths using Dijkstra's algorithm.

    Returns shortest paths to every node from a given source node.
    """
    if source_node not in graph:
        print("Invalid starting node.")
        return

    # all nodes initially are unvisited
    # all distances from source to a given node are infinity
    # previous node in optimal path from source is None
    unvisited, from_source, prev = set([]), {}, {}
    for node in graph:
        from_source[node] = float("inf")
        prev[node] = None
        unvisited.add(node)

    # set known distance from source_node to source_node
    from_source[source_node] = 0

    while unvisited:
        # pick unvisited node w/ least dist from source (greedy algo)
        # COULD USE A MIN PRIORITY QUEUE HERE INSTEAD
        shortest = float("inf")
        for node, dist in from_source.items():
            if node in unvisited and dist < shortest:
                current = node
                shortest = dist

        # remove it from unvisited
        unvisited.remove(current)

        # examine each of its unvisited neighbors
        # update distances (shorter paths update old)
        for neighbor, edge_weight in graph[current].items():
            if neighbor in unvisited:
                temp_dist = from_source[current] + edge_weight
                if temp_dist < from_source[neighbor]:
                    from_source[neighbor] = temp_dist
                    prev[neighbor] = current


    # return the shortest paths
    return from_source


def find_shortest_path(graph, source, target):
    """
    Find the shortest path between two nodes using Dijkstra's
    algorithm.

    Near identical to above implementation.
    """
    if source not in graph:
        print("Invalid starting node.")
        return
    elif target not in graph:
        print("Invalid target node.")
        return

    # all nodes initially are unvisited
    # all distances from source to a given node are infinity
    # previous node in optimal path from source is None
    unvisited, from_source, prev = set([]), {}, {}
    for node in graph:
        from_source[node] = float("inf")
        prev[node] = None
        unvisited.add(node)

    # set known distance from source to source
    from_source[source] = 0

    while unvisited:
        # pick unvisited node w/ least dist from source (greedy algo)
        # COULD USE A MIN PRIORITY QUEUE HERE INSTEAD
        shortest = float("inf")
        for node, dist in from_source.items():
            if node in unvisited and dist < shortest:
                current = node
                shortest = dist

        # remove it from unvisited
        unvisited.remove(current)

        # found target; exit while loop
        if current == target:
            break

        # examine each of its unvisited neighbors
        # update distances (shorter paths update old)
        for neighbor, edge_weight in graph[current].items():
            if neighbor in unvisited:
                temp_dist = from_source[current] + edge_weight
                if temp_dist < from_source[neighbor]:
                    from_source[neighbor] = temp_dist
                    prev[neighbor] = current


    # read shortest path from source to target by reverse iteration
    path = []
    if prev[target] or target == source:
        while target:
            path.append(target)
            target = prev[target]
    return path


if __name__ == '__main__':
    # print(find_shortest_paths(graph, 5))
    print(find_shortest_path(graph, 1, 4))