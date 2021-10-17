"""Sorted array to BST module"""

# problem statement: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
# # difficulty: easy

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solution class
    """

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums: List[int], left: int, right: int) -> TreeNode:
        """
        Builds the binary search tree for the given array.
        """
        if left > right:
            return None

        mid = left + (right - left) // 2

        root = TreeNode(nums[mid])
        root.left = self.build_tree(nums, left, mid - 1)
        root.right = self.build_tree(nums, mid + 1, right)

        return root


if __name__ == "__main__":
    solution = Solution()

    print(f"BST: {solution.sortedArrayToBST([-10,-3,0,5,9])}")
