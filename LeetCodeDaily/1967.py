"""
Number of Strings That Appear as Substrings in Word
"""

from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        result = 0

        for pattern in patterns:
            if pattern in word:
                result += 1

        return result


if __name__ == "__main__":
    testCases = [
        (["a", "abc", "bc", "d"], "abc", 3),
        (["a", "b", "c"], "aaaaabbbbb", 2),
        (["a", "a", "a"], "ab", 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().numOfStrings(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
