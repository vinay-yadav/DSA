"""
Valid Parentheses
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False

        closedBrackets = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in closedBrackets:
                if not stack or stack.pop() != closedBrackets[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    testCases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().isValid(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
