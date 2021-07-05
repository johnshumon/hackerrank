"""Reverse integer module:
Given an integer, function returns reversed version
of it if it's in the signed integer range;
0 otherwise
"""

# problem statement: https://leetcode.com/problems/reverse-integer
# difficulty: easy

import math


class Solution:
    def reverse(self, x: int) -> int:

        # checks if given integer is a 32-bit
        # signed integer.
        if not self.is_in_range(x):
            return 0

        # integer to string, reverse the
        # string and then converts it back
        # to integer
        number_str = str(abs(x))
        reversed_number = int(number_str[::-1])

        # makes reversed integer a negative integer
        # if given integer (i.e. x)is negative
        if x < 0:
            reversed_number = -reversed_number

        return 0 if not self.is_in_range(reversed_number) else reversed_number

    def is_in_range(self, x: int) -> bool:

        if x < int(math.pow(-2, 31)) or x > math.pow(2, 31) - 1:
            return False
        else:
            return True


def main():
    number = Solution()

    print(number.reverse(1534236469))


if __name__ == "__main__":
    main()
