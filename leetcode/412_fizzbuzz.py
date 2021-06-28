"""FizzBuzz solution module"""

# problem statement: https://leetcode.com/problems/fizz-buzz/

import math

from typing import List


class Solution:
    def fizzbuzz(self, n: int) -> List[str]:

        fizzbuzz_list = []
        if n <= 0 or n > math.pow(10, 4):
            return

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                fizzbuzz_list.append("FizzBuzz")
            elif i % 3 == 0:
                fizzbuzz_list.append("Fizz")
            elif i % 5 == 0:
                fizzbuzz_list.append("Buzz")
            else:
                fizzbuzz_list.append(f"{i}")

        return fizzbuzz_list


def main():
    fb = Solution()
    print(fb.fizzbuzz(15))


if __name__ == "__main__":
    main()
