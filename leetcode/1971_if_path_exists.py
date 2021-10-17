"""Graph path finding module"""

# problem statement: https://leetcode.com/problems/find-if-path-exists-in-graph
# # difficulty: easy

from collections import defaultdict
from typing import Dict, List, Optional, Set


class Solution:
    """Solution class"""

    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        """
        Returns true if there's a valid path bewteen
        'start & end' in a given list of edges. False
        otherwise.
        """

        # > case 1: if it's a one node graph then it's always true
        # > case 2: if it's a two node graph and there's an edge
        # between two nodes then this is always true as well.
        if n == 1 and [start, end] in edges:
            return True

        adj_list = defaultdict(set)

        # builds adjacency list out of list of edges.
        for node_1, node_2 in edges:
            adj_list[node_1].add(node_2)
            adj_list[node_2].add(node_1)

        visited = set()
        self.dfs(start, visited, adj_list)
        print(visited)
        return end in visited

    def dfs(self, current: int, visited: Set, adj_list: Dict) -> Optional:
        """
        DFS walk of the graph.
        """
        visited.add(current)

        for node in adj_list[current]:
            if node not in visited:
                self.dfs(node, visited, adj_list)


if __name__ == "__main__":
    solution = Solution()
    print(solution.validPath(1, [], 0, 0))
    print(solution.validPath(1, [[0, 1], [1, 2], [2, 0]], 0, 2))
    print(solution.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
