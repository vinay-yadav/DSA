"""
Remove Outermost Parentheses
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []

        balance = start = 0
        for idx, char in enumerate(s):
            if char == "(":
                balance += 1

                if balance == 1:
                    start = idx

            else:
                balance -= 1

            if balance == 0:
                result.append(s[start + 1 : idx])

        return "".join(result)


if __name__ == "__main__":
    testCases = [
        ("(()())(())", "()()()"),
        ("(()())(())(()(()))", "()()()()(())"),
        ("()()", ""),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().removeOuterParentheses(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
