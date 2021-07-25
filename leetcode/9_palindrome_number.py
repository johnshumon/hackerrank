"""Palindrome number module"""

# problem statement: https://leetcode.com/problems/palindrome-number
# # difficulty: easy

import math


class Solution:
    """checks if a given number is a palindrome"""

    def is_palindrome(self, x: int) -> bool:

        # checks if given number is in the range
        # of signed integer.
        if x < math.pow(-2, 31) or x > math.pow(2, 31):
            return False

        str_x = str(x)

        # > approach 1: chekcs str == reversed str
        # using string[::-1]
        # ** more pythonic way
        return str_x == str_x[::-1]

        # > approach 2: chekcs str == reversed str
        # by looping through front and back
        str_len = len(str_x)
        end = str_len - 1
        for i in range(str_len // 2):
            if str_x[i] != str_x[end - i]:
                return False
        return True


def main():
    number = Solution()

    # negative out of range
    result = number.is_palindrome(-91283472332)
    print(result)

    # positive out of range
    result = number.is_palindrome(91283472332)
    print(result)

    result = number.is_palindrome(123454321)
    print(result)


if __name__ == "__main__":
    main()
