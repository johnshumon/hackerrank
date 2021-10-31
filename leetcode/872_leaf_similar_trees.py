"""Max depth of a binary tree module"""

# problem statement: https://leetcode.com/problems/leaf-similar-trees
# difficulty: easy

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leaf_similar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # True if list of both tree's leaf nodes are equal
        # False otherwise.
        return self.find_leafs(root1, []) == self.find_leafs(root2, [])

    def find_leafs(self, node: TreeNode, leafs: List) -> List:
        """
        Helper function. Recursively finds all the leafs
        of the given sub-tree.
        """
        if node is None:
            return

        if node.left is None and node.right is None:
            leafs.append(node.val)

        self.find_leafs(node.left, leafs)
        self.find_leafs(node.right, leafs)

        return leafs


if __name__ == "__main__":
    solution = Solution()

    # TODO: construct the tree using following lists.
    # ref: https://www.section.io/engineering-education/binary-tree-data-structure-python
    # e.g.: root = TreeNode, root.left = TreeNode(5), root.right(1)

    solution.leaf_similar([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4], [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
