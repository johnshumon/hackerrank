"""Binary tree Postorder traversal module"""

# problem statement: https://leetcode.com/problems/binary-tree-postorder-traversal
# # difficulty: easy

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """Returns pre-order traversal list of a given BST.
        > Traverse order: root -> left -> right
        """
        elements = []

        if root is None:
            return None

        if root.left:
            elements += self.postorder_traversal(root.left)

        if root.right:
            elements += self.postorder_traversal(root.right)

        elements.append(root.val)

        return elements
