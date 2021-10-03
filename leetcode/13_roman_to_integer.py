"""Roman to integer module"""

# problem statement: https://leetcode.com/problems/roman-to-integer/
# # difficulty: easy


class Solution:
    """
    Solution class
    """
    def roman_to_int(self, s: str) -> int:
        """
        Returns integer value of the given roman numeral.
        """
        str_len = len(s)
        result = 0
        i = 0
        while i < str_len:

            current_number = self.numeric_lookup(s[i])

            # if its the last element in the string
            # then string[i+1] would cause index out
            # range error.
            if i != str_len - 1:
                next_number = self.numeric_lookup(s[i + 1])

            # if it's the last numeral in the given
            # string then there's no next numeral to
            # compare with.
            if i == str_len - 1:
                next_number = 0

            # if a current numeral in the string is
            # smaller than next one then result
            # will be "next - current". As both
            # current and next numerals would be
            # processed once deduction is executed,
            # therefore next i value would be i+2
            # i.e. next of greater numeral's index.
            # ------------------------------------
            if current_number < next_number:
                result += next_number - current_number
                i += 2

            else:
                result += current_number
                i += 1

        return result

    def numeric_lookup(self, roman_numeral: str) -> int:
        lookups = {
            "I": 1,
            "V": 5,
            "VIIII": 9,
            "X": 10,
            "XXXX": 40,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        return lookups[roman_numeral] if roman_numeral in lookups else 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.roman_to_int("") == 0
    assert solution.roman_to_int("IV") == 4
    assert solution.roman_to_int("VI") == 6
    assert solution.roman_to_int("XCIV") == 94
    assert solution.roman_to_int("MCDLXXIV") == 1474
    assert solution.roman_to_int("MMCDLIX") == 2459
    assert solution.roman_to_int("MMCDXXI") == 2421
    assert solution.roman_to_int("MDCXCV") == 1695
