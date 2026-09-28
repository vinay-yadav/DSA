"""
Maximum Nesting Depth of the Parentheses
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0

        count = 0
        for char in s:
            if char == "(":
                count += 1

            elif char == ")":
                max_depth = max(max_depth, count)
                count -= 1

        return max_depth


if __name__ == "__main__":
    testCases = [
        ("(1+(2*3)+((8)/4))+1", 3),
        ("(1)+((2))+(((3)))", 3),
        ("()(())((()()))", 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxDepth(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
