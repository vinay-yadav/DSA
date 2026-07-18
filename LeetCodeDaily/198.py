"""
House Robber
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        self.dp = [-1 for _ in range(n + 1)]
        return self.topDown(n, nums)

    def topDown(self, n, nums) -> int:
        if n < 0:
            return 0

        if self.dp[n] != -1:
            return self.dp[n]

        self.dp[n] = max(
            self.topDown(n - 1, nums), self.topDown(n - 2, nums) + nums[n - 1]
        )

        return self.dp[n]


if __name__ == "__main__":
    testCases = [([1, 2, 3, 1], 4), ([2, 7, 9, 3, 1], 12)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().rob(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
