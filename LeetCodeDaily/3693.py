"""
Climbing Stairs II
"""

import sys


class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [-1] * (n + 1)

        def solve(i):
            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]

            ans = min(
                solve(j) + costs[j - 1] + (j - i) * (j - i)
                for j in range(i + 1, min(i + 3, n) + 1)
            )

            dp[i] = ans

            return ans

        return solve(0)

    def climbStairs1(self, n: int, costs: list[int]) -> int:
        dp = [-1] * (n + 1)

        def solve(i):
            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]

            cost = sys.maxsize

            j = i + 1
            if j <= n:
                cost = min(cost, solve(j) + costs[j - 1] + (j - i) * (j - i))

            j = i + 2
            if j <= n:
                cost = min(cost, solve(j) + costs[j - 1] + (j - i) * (j - i))

            j = i + 3
            if j <= n:
                cost = min(cost, solve(j) + costs[j - 1] + (j - i) * (j - i))

            dp[i] = cost

            return cost

        return solve(0)


if __name__ == "__main__":
    testCases = [
        (4, [1, 2, 3, 4], 13),
        (4, [5, 1, 6, 2], 11),
        (3, [9, 8, 3], 12),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().climbStairs(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
