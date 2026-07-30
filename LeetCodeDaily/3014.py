"""
Minimum Number of Pushes to Type Word I
"""


class Solution:
    def minimumPushes(self, word: str) -> int:
        result = 0
        for idx in range(len(word)):
            result += (idx // 8) + 1

        return result


if __name__ == "__main__":
    testCases = [
        ("abcde", 5),
        ("xycdefghij", 12),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minimumPushes(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
