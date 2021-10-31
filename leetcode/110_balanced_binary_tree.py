"""Max depth of a binary tree module"""

# problem statement: https://leetcode.com/problems/balanced-binary-tree
# difficulty: easy

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        if abs(self.tree_height(root.left) - self.tree_height(root.right)) <= 1:
            return self.is_balanced(root.left) and self.is_balanced(root.right)

        return False

    def tree_height(self, node: TreeNode) -> int:

        if node is None:
            return 0

        return max(self.tree_height(node.left), self.tree_height(node.right)) + 1


if __name__ == "__main__":
    solution = Solution()

    # TODO: construct the tree using following lists.
    # ref: https://www.section.io/engineering-education/binary-tree-data-structure-python
    # e.g.: root = TreeNode, root.left = TreeNode(5), root.right(1)

    solution.is_balanced([3, 9, 20, None, None, 15, 7])
