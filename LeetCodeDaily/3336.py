"""
Find the Number of Subsequences With Equal GCD
"""

import math
from typing import List


class Solution:
    MOD = 1_000_000_007

    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)
        maxNum = max(nums)
        self.dp = [
            [[-1 for _ in range(maxNum + 1)] for _ in range(maxNum + 1)]
            for _ in range(n + 1)
        ]
        return self.solve(nums, 0, 0, 0)

    def solve(self, nums, position, gcd_1, gcd_2):
        if len(nums) == position:
            if gcd_1 == 0 or gcd_2 == 0:
                return 0

            if gcd_1 == gcd_2:
                return 1

            return 0

        if self.dp[position][gcd_1][gcd_2] != -1:
            return self.dp[position][gcd_1][gcd_2]

        skip = self.solve(nums, position + 1, gcd_1, gcd_2)
        seq_1 = self.solve(nums, position + 1, math.gcd(gcd_1, nums[position]), gcd_2)
        seq_2 = self.solve(nums, position + 1, gcd_1, math.gcd(gcd_2, nums[position]))

        self.dp[position][gcd_1][gcd_2] = (skip + seq_1 + seq_2) % self.MOD
        return self.dp[position][gcd_1][gcd_2]

    def gcd(self, a, b):
        if b == 0:
            return a

        return self.gcd(b, a % b)


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3, 4], 10),
        ([10, 20, 30], 2),
        ([1, 1, 1, 1], 50),
        ([10, 10, 20, 12, 11, 17, 12], 380),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().subsequencePairCount(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
