"""
Minimum Number of Squares
"""


class Solution:
    def solve(self, num):
        self.dp = [-1] * (num + 1)
        self.dp[0] = 0

        # return self.topDown(num)
        return self.bottomUp(num)

    def topDown(self, n):
        if self.dp[n] != -1:
            return self.dp[n]

        ans = float("inf")
        i = 1
        while (sqaure := i * i) <= n:
            ans = min(ans, self.topDown(n - (sqaure)))
            i += 1

        self.dp[n] = ans + 1
        return ans + 1

    def bottomUp(self, num):
        dp = [float("inf")] * (num + 1)
        dp[0] = 0

        for i in range(1, num + 1):
            j = 1
            while (square := j * j) <= i:
                dp[i] = min(dp[i], dp[i - square] + 1)
                j += 1

        return dp[-1]


if __name__ == "__main__":
    testCases = [(4, 1), (12, 3)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
