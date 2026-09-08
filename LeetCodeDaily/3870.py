"""
Count Commas in Range
"""


class Solution:
    def countCommas(self, n: int) -> int:
        return max(n - 999, 0)


if __name__ == "__main__":
    testCases = [
        (1002, 3),
        (998, 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countCommas(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
