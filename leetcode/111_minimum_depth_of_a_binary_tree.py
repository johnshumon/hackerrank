"""Min depth of a binary tree module"""

# problem statement: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# difficulty: easy

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution class"""

    def min_depth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

            # initialize the queue with the tree
        queue = [root]
        depth = 0

        while queue:
            inner_queue = []
            depth += 1

            # traverse through the queue
            for node in queue:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    inner_queue.append(node.left)
                if node.right:
                    inner_queue.append(node.right)

            queue = inner_queue


if __name__ == "__main__":
    solution = Solution()
    print("min-depth: ", solution.max_depth([3, 9, 20, None, None, 15, 7]))
