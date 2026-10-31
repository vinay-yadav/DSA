"""
Twisted Mirror Path Count
"""


class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 1_000_000_007
        RIGHT, DOWN = 0, 1

        dp = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(m)]

        def solve(i, j, d) -> int:
            if i == m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n:
                return 0

            if dp[i][j][d] != -1:
                return dp[i][j][d]

            if grid[i][j] == 1:
                if d == RIGHT:
                    ans = solve(i + 1, j, DOWN)
                else:
                    ans = solve(i, j + 1, RIGHT)
            else:
                ans = (solve(i + 1, j, DOWN) + solve(i, j + 1, RIGHT)) % MOD

            dp[i][j][d] = ans

            return ans

        return (solve(0, 1, RIGHT) + solve(1, 0, DOWN)) % MOD


if __name__ == "__main__":
    testCases = [
        ([[0, 1, 0], [0, 0, 1], [1, 0, 0]], 5),
        ([[0, 0], [0, 0]], 2),
        ([[0, 1, 1], [1, 1, 0]], 1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().uniquePaths(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
