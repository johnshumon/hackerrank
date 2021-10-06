"""
Directed graph module
"""

# Corner cases
# -------------
# Empty graph
# Graph with one or two nodes
# Disjoint graphs
# Graph with cycles

from collections import defaultdict
from typing import Any, Dict, List, Set


class DGraph:
    """
    Directed Graph.

    Represents edges between arbitrary objects called nodes.
    """

    def __init__(self):
        self.adj_list = defaultdict(set)

    def connect_edges(self, *edges) -> Dict:
        """
        Builds graph for the given edges.

        Accepts arbitrary number of paris (u, v), meaning
        there's an edge in the graph from u -> v.
        """

        # TODO: sanity check for empty list of tuples

        for start, end in edges:
            if start in self.adj_list:
                self.adj_list[start].append(end)
            else:
                self.adj_list[start] = [end]

        return self.adj_list

    def get_paths(self, start: Any, end: Any, visited: List) -> List:
        """
        Returns all paths between two nodes.

        Accepts a pair (u, v) and finds all the possible
        paths between u -> v if any.
        """

        # 'start' not in the dictionary key means
        # there's no edge coming out of that node.
        if start not in self.adj_list:
            return []

        visited = visited + [start]

        # print(f"visited: {visited}")

        if start == end:
            return [visited]

        paths = []

        # For all the adjacent nodes of 'start'
        # recur this function.
        for node in self.adj_list[start]:
            if node not in visited:
                sub_paths = self.get_paths(node, end, visited)

                for item in sub_paths:
                    paths.append(item)

        return paths

    def get_shortest_path(self, start: Any, end: Any) -> List:
        """
        Returns shortest path between two nodes.

        Accepts a pair (u, v), finds all the possible
        paths between u -> v from 'get_path' method if
        any. And then returns the shortest one.
        """

        # 'key' argument finds the min/max of an iterable based
        # on what is defined as a key. Here key is length. Hence,
        # of all the lists, min length list is returned.
        return min(self.get_paths(start, end, []), key=len)

#     def is_disjoint():
#         pass


def dfs_traversal(graph: DGraph, node: Any, visited: List[Any]) -> Set:
    """
    Does depth first search (DFS) over a graph.

    Begins with the starting node and returns the
    DFS traversal order of the nodes in the graph.
    """

    if node is None or graph is None:
        return visited

    if node not in visited:
        # Set unions. list is used to keep the traversal
        # order correct. Because both 'union & set.add'
        # different order in different times.
        visited.append(node)

        for neighbour in graph.adj_list[node]:
            dfs_traversal(graph, neighbour, visited)

    return visited


# def bfs_walk():
#     pass


if __name__ == "__main__":

    dg = DGraph()
    # dg.connect_edges(("a", "b"), ("a", "d"), ("b", "a"), ("b", "c"))
    # dg.connect_edges(("c", "b"), ("c", "d"), ("d", "a"), ("d", "c"))
    # dg.connect_edges(("e", "f"), ("e", "a"))

    dg.connect_edges(("a", "b"), ("a", "c"), ("a", "e"))
    dg.connect_edges(("b", "d"), ("b", "e"), ("c", "e"), ("d", "c"))
    # dg.connect_edges("")

    print(f"Adjacency-list: {dg.adj_list}")

    print(f"Paths between 'a' & 'c' are: {dg.get_paths('a', 'c', [])}")
    print(f"Shortest path between 'a' & 'c' are: {dg.get_shortest_path('a', 'c')}")
    print(f"DFS walk of the graph: {dfs_traversal(dg, 'a', [])}")
