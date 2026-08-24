"""
Stone Game VIII
"""


class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)

        for i in range(1, n):
            stones[i] = stones[i] + stones[i - 1]

        dp = [0] * n
        dp[n - 1] = stones[n - 1]

        for idx in range(n - 2, 0, -1):
            take = stones[idx] - dp[idx + 1]
            skip = dp[idx + 1]

            dp[idx] = max(take, skip)

        return dp[1]

    def stoneGameVIII_TOP_DOWN(self, stones: list[int]) -> int:
        n = len(stones)
        dp = [float("-inf")] * (n + 1)

        for i in range(1, n):
            stones[i] = stones[i] + stones[i - 1]

        def solve(idx):
            if idx == n - 1:
                return stones[idx]

            if dp[idx] != float("-inf"):
                return dp[idx]

            take = stones[idx] - solve(idx + 1)
            skip = solve(idx + 1)

            dp[idx] = max(take, skip)

            return dp[idx]

        return solve(1)  # type: ignore


if __name__ == "__main__":
    testCases = [
        ([-1, 2, -3, 4, -5], 5),
        ([7, -6, 5, 10, 5, -2, -6], 13),
        ([-10, -12], -22),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().stoneGameVIII(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
