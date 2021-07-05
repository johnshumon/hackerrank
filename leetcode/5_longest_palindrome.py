"""Longest palindrome subsequence (LPS) module"""

# problem statement: https://leetcode.com/problems/longest-palindromic-substring
# difficulty: medium


class Solution:
    def longest_palindrome_subseq(self, given_str: str) -> str:
        str_length = len(given_str)

        start = 0

        palindrome_table = [[0 for x in range(str_length)] for y in range(str_length)]

        # case 1: sub-string of length 1
        # > fill diagonal position i.e. substring of
        #   length 1 as true.
        # -------------------------------------------
        max_length = 1
        for i in range(str_length):
            palindrome_table[i][i] = True

        # case 2: sub-string of length 2
        # > check if substring at index i & i+1
        #   Fill [i][i+1] as true if both are same.
        # -------------------------------------------
        for i in range(str_length - 1):
            if given_str[i] == given_str[i + 1]:
                palindrome_table[i][i + 1] = True
                start = i
                max_length = 2

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

                    if sub_str_len > max_length:
                        max_length = sub_str_len
                        start = i

        result = self.find_longest_substr(given_str, start, start + max_length - 1)
        return result

    def find_longest_substr(self, s: str, start: int, end: int) -> str:
        return s[start : end + 1]


def main():

    string = "babad"
    lps = Solution()

    print("String is:", lps.longest_palindrome_subseq(string))


if __name__ == "__main__":
    main()
