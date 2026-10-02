"""
Generate Parentheses
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        path = []

        def backtrack(open_used: int, close_used: int):
            if close_used == n:
                result.append("".join(path))
                return

            if open_used < n:
                path.append("(")
                backtrack(open_used + 1, close_used)
                path.pop()

            if close_used < open_used:
                path.append(")")
                backtrack(open_used, close_used + 1)
                path.pop()

        backtrack(0, 0)

        return result

    def generateParenthesis1(self, n: int) -> list[str]:
        result = []

        def recursion(brackets: list, open_used: int, close_used: int):
            if close_used == n:
                generated_paranthesis = "".join(brackets)
                result.append(generated_paranthesis)
                return

            if open_used < n:
                # open
                recursion(brackets + ["("], open_used + 1, close_used)

            if close_used < open_used:
                # close
                recursion(brackets + [")"], open_used, close_used + 1)

        recursion([], 0, 0)

        return result


if __name__ == "__main__":
    testCases = [
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (1, ["()"]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().generateParenthesis(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
