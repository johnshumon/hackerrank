"""Palindromic substrings module.
Given a string s, return the number
of palindromic substrings in it.
"""

# problem statement: https://leetcode.com/problems/palindromic-substrings/
# difficulty: medium


class Solution:
    def count_substrings(self, given_str: str) -> str:

        str_length = len(given_str)
        counter = 0

        palindrome_table = [[0 for x in range(str_length)] for y in range(str_length)]

        # case 1: sub-string of length 1
        # > fill diagonal position i.e. substring of
        #   length 1 as true.
        # -------------------------------------------
        for i in range(str_length):
            palindrome_table[i][i] = True
            counter += 1

        # case 2: sub-string of length 2
        # > check if substring at index i & i+1
        #   Fill [i][i+1] as true if both are same.
        # -------------------------------------------
        for i in range(str_length - 1):
            if given_str[i] == given_str[i + 1]:
                palindrome_table[i][i + 1] = True
                counter += 1

        # case 3: sub-string of length > 2
        # > given_str[i][j] is palindrome if:
        #   given_str[i] == given_str[j] and
        #   palindrome[i + 1][j - 1] is True
        for sub_str_len in range(3, str_length + 1):
            for i in range(str_length - sub_str_len + 1):

                # end index of the substring
                j = i + sub_str_len - 1

                if (
                    given_str[i] == given_str[j]
                    and palindrome_table[i + 1][j - 1] is True
                ):
                    palindrome_table[i][j] = True
                    counter += 1

        return counter


def main():

    string = "aaaaa"
    lps = Solution()

    print("Total sub-strings are:", lps.count_substrings(string))


if __name__ == "__main__":
    main()
