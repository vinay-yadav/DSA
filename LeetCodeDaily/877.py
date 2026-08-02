"""
Stone Game
"""


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        # As per the given constraints, ALice will always win
        return True

    def stoneGame1(self, piles: list[int]) -> bool:
        n = len(piles)
        dp = [[float("-inf") for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        def func(i, j):
            if dp[i][j] != float("-inf"):
                return dp[i][j]

            dp[i][j] = max(piles[i] - func(i + 1, j), piles[j] - func(i, j - 1))

            return dp[i][j]

        return True if func(0, n - 1) > 0 else False


if __name__ == "__main__":
    testCases = [
        ([5, 3, 4, 5], True),
        ([3, 7, 2, 3], True),
        ([1, 5, 5, 2], True),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().stoneGame(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
