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


class DGraph:
    """
    Directed Graph.

    Represents edges between arbitrary objects called nodes.
    """

    def __init__(self):
        self.adj_list = defaultdict(set)

    def connect_edges(self, *edges) -> dict:
        """
        Builds graph for the given edges.

        Accepts arbitrary number of paris (u, v), meaning
        there's an edge in the graph from u -> v.
        """

        for start, end in edges:
            if start in self.adj_list:
                self.adj_list[start].append(end)
            else:
                self.adj_list[start] = [end]

        return self.adj_list

#     def get_paths():
#         pass

#     def get_shortest_path():
#         pass

#     def is_disjoint():
#         pass


# def dfs_traversal():
#     pass

# def bfs_walk():
#     pass


if __name__ == "__main__":

    dg = DGraph()
    dg.connect_edges(("a", "b"), ("a", "d"), ("b", "a"), ("b", "c"))
    dg.connect_edges(("c", "b"), ("c", "d"), ("d", "a"), ("d", "c"))
    dg.connect_edges(("e", "f"), ("e", "a"))

    print(f"Adjacency-list: {dg.adj_list}")
