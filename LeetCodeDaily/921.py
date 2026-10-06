"""
Minimum Add to Make Parentheses Valid
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        required = 0

        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    required += 1

        required += len(stack)
        return required


if __name__ == "__main__":
    testCases = [
        ("())", 1),
        ("(((", 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minAddToMakeValid(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
