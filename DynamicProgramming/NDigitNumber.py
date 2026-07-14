"""
N digit Numbers
"""


class Solution:
    def solve(self, A, B):
        self.dp = [[-1 for _ in range(B + 1)] for _ in range(A + 1)]
        self.dp[1][0] = 0

        for i in range(1, 10):
            if i > B:
                break
            self.dp[1][i] = 1

        for i in range(10, B + 1):
            self.dp[1][i] = 0

        # return self.topDown(A, B)
        return self.bottomUp(A, B)

    def topDown(self, n, s):
        if self.dp[n][s] != -1:
            return self.dp[n][s]

        nums = 0
        for i in range(10):
            if i < s:
                nums += self.topDown(n - 1, s - i)

        self.dp[n][s] = nums
        return nums

    def bottomUp(self, n, s):
        dp = [[0 for _ in range(s + 1)] for _ in range(n + 1)]

        for i in range(1, 10):
            if i > s:
                break
            dp[1][i] = 1

        for i in range(10, s + 1):
            dp[1][i] = 1

        for i in range(2, n + 1):
            for j in range(1, s + 1):
                ans = 0
                for d in range(0, 9):
                    if j > d:
                        ans += dp[i - 1][j - d]

                dp[i][j] = ans

        return dp[n][s]


if __name__ == "__main__":
    testCases = [(1, 5, 1), (2, 4, 4), (3, 3, 6)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
