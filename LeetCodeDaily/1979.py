"""
Sorted GCD Pair Queries
"""

import math


class Solution:
    def findGCD(self, nums: list[int]) -> int:
        return math.gcd(min(nums), max(nums))


if __name__ == "__main__":
    testCases = [([2, 5, 6, 9, 10], 2), ([7, 5, 6, 8, 3], 1), ([3, 3], 3)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findGCD(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
