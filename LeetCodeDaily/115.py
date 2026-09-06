"""
Distinct Subsequences
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for j in range(1, m + 1):
            dp[0][j] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]

                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[n][m]

    def numDistinct1(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        def solve(i, j) -> int:
            if j == 0:
                dp[i][j] = 1
                return dp[i][j]

            if i == 0:
                dp[i][j] = 0
                return dp[i][j]

            if dp[i][j] != -1:
                return dp[i][j]

            ans = solve(i - 1, j)

            if s[i - 1] == t[j - 1]:
                ans += solve(i - 1, j - 1)

            dp[i][j] = ans

            return dp[i][j]

        return solve(n, m)


if __name__ == "__main__":
    testCases = [
        ("rabbbit", "rabbit", 3),
        ("babgbag", "bag", 5),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().numDistinct(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
