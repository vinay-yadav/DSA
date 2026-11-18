"""
Minimum Number of Changes to Make Binary String Beautiful
"""


class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        operations = 0

        for idx in range(0, n, 2):
            if s[idx] != s[idx + 1]:
                operations += 1

        return operations


if __name__ == "__main__":
    testCases = [
        ("1001", 2),
        ("10", 1),
        ("0000", 0),
        ("110011", 0),
        ("11000111", 1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minChanges(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
