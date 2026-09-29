"""
Check if There Is a Valid Parentheses String Path
"""


class Solution:
    MAX_M = 101
    MAX_N = 101

    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 == 1 or grid[0][0] == ")" or grid[m - 1][n - 1] == "(":
            return False

        dp = [
            [
                [None for _ in range(self.MAX_M + self.MAX_N)]
                for _ in range(self.MAX_N + 1)
            ]
            for _ in range(self.MAX_M + 1)
        ]

        def backtracking(i, j, openCount) -> bool:
            if grid[i][j] == "(":
                openCount += 1
            else:
                openCount -= 1

            if openCount < 0:
                return False

            if dp[i][j][openCount] is not None:
                return dp[i][j][openCount]

            if i == m - 1 and j == n - 1:
                dp[i][j][openCount] = openCount == 0
                return dp[i][j][openCount]

            dp[i][j][openCount] = False

            for p, q in [(1, 0), (0, 1)]:
                ni, nj = p + i, q + j

                if ni < 0 or ni == m or nj < 0 or nj == n:
                    continue

                if backtracking(ni, nj, openCount):
                    dp[i][j][openCount] = True
                    return dp[i][j][openCount]

            return dp[i][j][openCount]

        return backtracking(0, 0, 0)


if __name__ == "__main__":
    testCases = [
        ([["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]], True),
        ([[")", ")"], ["(", "("]], False),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().hasValidPath(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
