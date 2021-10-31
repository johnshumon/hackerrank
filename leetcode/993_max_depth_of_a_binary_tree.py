"""Max depth of a binary tree module"""

# problem statement: https://leetcode.com/problems/maximum-depth-of-binary-tree
# difficulty: easy

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution class"""

    def max_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    solution = Solution()

    # TODO: construct the tree using following lists.
    # ref: https://www.section.io/engineering-education/binary-tree-data-structure-python
    # e.g.: root = TreeNode, root.left = TreeNode(5), root.right(1)

    solution.max_depth([3, 9, 20, None, None, 15, 7])
