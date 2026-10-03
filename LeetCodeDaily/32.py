"""
Longest Valid Parentheses
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        n = len(s)
        longest_parentheses = 0

        open = close = 0
        # left to right
        for idx in range(n):
            char = s[idx]

            if char == "(":
                open += 1
            else:
                close += 1

            if open == close:
                longest_parentheses = max(longest_parentheses, open + close)
            elif close > open:
                open = close = 0

        open = close = 0
        # right to left
        for idx in range(n - 1, -1, -1):
            char = s[idx]

            if char == "(":
                open += 1
            else:
                close += 1

            if open == close:
                longest_parentheses = max(longest_parentheses, open + close)
            elif close < open:
                open = close = 0

        return longest_parentheses

    def bruteForce(self, s: str) -> int:
        """
        TC: O(n^2)
        SC: O(1)
        """
        n = len(s)

        longest_parentheses = 0

        for i in range(n):
            balance = 0
            for j in range(i, n):
                if s[j] == "(":
                    balance += 1
                else:
                    balance -= 1

                if balance == 0:
                    longest_parentheses = max(longest_parentheses, j - i + 1)
                elif balance < 0:
                    break

        return longest_parentheses


if __name__ == "__main__":
    testCases = [
        ("(()", 2),
        (")()())", 4),
        ("", 0),
        (")(", 0),
        ("(((((", 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().longestValidParentheses(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
