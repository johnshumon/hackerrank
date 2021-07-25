"""Valid palindrome checking module"""

# problem statement: https://leetcode.com/problems/valid-palindrome/submissions
# difficulty: easy


class Solution:
    def is_palindrome(self, s: str) -> bool:

        parsed_str = ""

        for char in s:
            if char.isalnum():
                parsed_str = "".join([parsed_str, char.lower()])

        if parsed_str == parsed_str[::-1]:
            return True
        else:
            return False


def main():
    check = Solution()

    print(check.is_palindrome("A man, a plan, a canal: Panama"))
    print(check.is_palindrome("race a car"))


if __name__ == "__main__":
    main()
