"""
Minimum XOR Path in a Grid
"""


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j] = int whose bit x is 1 if XOR value x is reachable at (i, j)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 << grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                up = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0

                combined = up | left  # OR of both predecessors

                for xor_val in range(1024):
                    if (combined >> xor_val) & 1:
                        dp[i][j] |= 1 << (xor_val ^ grid[i][j])

        # smallest reachable XOR value at the bottom-right cell
        last = dp[m - 1][n - 1]
        for xor_val in range(1024):
            if (last >> xor_val) & 1:
                return xor_val

        return -1


if __name__ == "__main__":
    testCases = [
        ([[1, 2], [3, 4]], 6),
        ([[6, 7], [5, 8]], 9),
        ([[2, 7, 5]], 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minCost(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
