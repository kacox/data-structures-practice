"""
A simple (class-free) graph implementation.

         0 -- 1
        /      \ 
       4 ------ 2 -- 3 -- 5



"""

import sys
import random


# adjacency list
graph = {0: set([1, 4]),
            1: set([0, 2]),
            2: set([1, 3, 4]),
            3: set([2, 5]),
            4: set([0, 2]),
            5: set([3])}


def bfs(graph):
    if graph:
        q = []
        visited = set()

        start = random.choice(list(graph.keys()))
        q.append(start)
        visited.add(start)
        while q:
            current_node = q.pop(0) 
            print(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)


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


if __name__ == '__main__':
    # bfs(graph)
    dfs(graph)