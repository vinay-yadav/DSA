"""
Minimum Number of Pushes to Type Word II
"""

from collections import defaultdict


class Solution:
    def minimumPushes(self, word: str) -> int:
        count = defaultdict(int)

        for ch in word:
            count[ch] += 1

        sorted_chars = sorted(count, key=lambda x: -count[x])

        result = 0
        for idx, ch in enumerate(sorted_chars):
            result += count[ch] * ((idx // 8) + 1)

        return result


if __name__ == "__main__":
    testCases = [
        ("abcde", 5),
        ("xyzxyzxyzxyz", 12),
        ("aabbccddeeffgghhiiiiii", 24),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minimumPushes(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
