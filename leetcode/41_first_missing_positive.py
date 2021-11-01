"""First positive integer module"""

# problem statement: https://leetcode.com/problems/find-if-path-exists-in-graph
# difficulty: hard

from collections import defaultdict
from typing import List


class Solution:
    def first_missing_positive(self, nums: List[int]) -> int:

        # converts nums to a set
        lookups = set(nums)
        i = 1

        # looks up in the set
        while i in lookups:
            i += 1

        # returns 1 for any negative list of integers
        return i


if __name__ == "__main__":
    solution = Solution()
    print("missing-int: ", solution.first_missing_positive([0, 1, 2]))
    print("missing-int: ", solution.first_missing_positive([-1, -2]))
