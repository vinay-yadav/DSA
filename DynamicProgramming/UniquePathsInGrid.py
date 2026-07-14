"""
Unique Paths In Grid
"""


class Solution:
    def solve(self, A, B):
        self.dp = [[-1 for _ in range(B)] for _ in range(A)]

        for i in range(B):
            self.dp[0][i] = 1

        for i in range(A):
            self.dp[i][0] = 1

        return self.topDown(A - 1, B - 1)

    def topDown(self, n, m):
        if self.dp[n][m] != -1:
            return self.dp[n][m]

        self.dp[n][m] = self.topDown(n - 1, m) + self.topDown(n, m - 1)

        return self.dp[n][m]

    def bottomUp(self, n, s): ...


if __name__ == "__main__":
    testCases = [(5, 4, 35)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
