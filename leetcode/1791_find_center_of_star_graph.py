"""Find center of the star graph module"""

# problem statement: https://leetcode.com/problems/find-center-of-star-graph
# difficulty: easy

from collections import defaultdict
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        adj_list = defaultdict(set)

        # creates adjacency list out of edges list
        for node_1, node_2 in edges:
            adj_list[node_1].add(node_2)
            adj_list[node_2].add(node_1)

        # key which has edges to all other nodes is
        # key in the center.
        for key, value in adj_list.items():
            if len(value) == len(edges):
                return key


if __name__ == "__main__":
    solution = Solution()
    print(solution.findCenter([[1, 2], [2, 3], [4, 2]]))
