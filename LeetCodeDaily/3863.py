"""
Minimum Operations to Sort a String
"""


class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # already sorted string
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        if n == 2:
            return -1

        min_char = min(s)
        max_char = max(s)

        if s[0] == min_char or s[-1] == max_char:
            return 1

        mid = s[1:-1]
        if min_char in mid or max_char in mid:
            return 2

        return 3


if __name__ == "__main__":
    testCases = [
        ("dog", 1),
        ("card", 2),
        ("gf", -1),
        ("cba", 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minOperations(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
