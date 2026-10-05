"""
Score of Parentheses
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        depth = score = 0
        for idx, char in enumerate(s):
            if char == "(":
                depth += 1
            else:
                depth -= 1
                if s[idx - 1] == "(":
                    score += 1 << depth

        return score

    def scoreOfParentheses1(self, s: str) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        stack = []
        score = 0

        for idx, char in enumerate(s):
            if char == "(":
                stack.append(score)
                score = 0
            else:
                if s[idx - 1] == "(":
                    score = stack[-1] + 1
                else:
                    score = stack[-1] + 2 * score

                stack.pop()

        return score


if __name__ == "__main__":
    testCases = [
        ("((()))", 4),
        ("(()(()))", 6),
        ("()", 1),
        ("(())", 2),
        ("()()", 2),
        ("(())", 2),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().scoreOfParentheses(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
