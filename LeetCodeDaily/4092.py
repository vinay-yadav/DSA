"""
Binary Digit Score
"""


class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1 = s2 = 0

        for idx in range(32):
            if a & 1 << idx:
                s1 += 1

            if b & 1 << idx:
                s2 += 1

        if s1 >= s2:
            return s1 * s2

        return s2 // s1


if __name__ == "__main__":
    testCases = [
        (14, 6, 6),
        (5, 15, 2),
        (10, 12, 4),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().calculateScore(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
