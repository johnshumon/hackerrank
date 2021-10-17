"""Reverse Polish Notation module"""

# problem statement: https://leetcode.com/problems/evaluate-reverse-polish-notation
# difficulty: medium

from typing import List


class Solution:
    def eval_rpn(self, tokens: List[str]) -> int:

        if len(tokens) < 1 or len(tokens) > (10 ** 4):
            return -1

        result = []

        for token in tokens:
            if token in "+-*/":
                op_2, op_1 = result.pop(), result.pop()
                result.append(self.calculate(token, op_1, op_2))
            else:
                result.append(int(token))

        return result.pop()

    @staticmethod
    def calculate(operator: str, operand_1: int, operand_2: int) -> int:

        if operator == "+":
            return operand_1 + operand_2
        elif operator == "-":
            return operand_1 - operand_2
        elif operator == "*":
            return operand_1 * operand_2
        elif operator == "/":
            if operand_1 < 0 < operand_2 or operand_1 > 0 > operand_2:
                return -(abs(operand_1) // abs(operand_2))
            return operand_1 // operand_2


if __name__ == "__main__":
    solution = Solution()

    print(
        solution.eval_rpn(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
    )
    print(solution.eval_rpn(["4", "13", "5", "/", "+"]))
