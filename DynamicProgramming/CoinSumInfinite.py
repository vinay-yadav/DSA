"""
Coin Sum Infinite
"""


class Solution:
    MOD = 1000007

    def solve(self, A, B):
        n = len(A)
        self.dp = [[-1 for _ in range(B + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            self.dp[i][0] = 1

        for i in range(1, B + 1):
            self.dp[0][i] = 0

        return self.bottomUp(n, B, A)
        # return self.topDown(n, B, A)

    def topDown(self, position, remainingCapacity, arr):
        if self.dp[position][remainingCapacity] != -1:
            return self.dp[position][remainingCapacity]

        coinValue = arr[position - 1]
        if coinValue <= remainingCapacity:
            ways = (
                self.topDown(position - 1, remainingCapacity, arr)
                + self.topDown(position, remainingCapacity - coinValue, arr)
            ) % self.MOD
        else:
            ways = self.topDown(position - 1, remainingCapacity, arr)

        self.dp[position][remainingCapacity] = ways
        return ways

    def bottomUp(self, position, remainingCapacity, arr):
        dp = [0] * (remainingCapacity + 1)
        dp[0] = 1

        for i in range(1, position + 1):
            coinValue = arr[i - 1]
            for j in range(coinValue, remainingCapacity + 1):
                dp[j] = (dp[j] + dp[j - coinValue]) % self.MOD

        return dp[-1]

    def bottomUp2(self, position, remainingCapacity, arr):
        for i in range(1, position + 1):
            coinValue = arr[i - 1]

            for j in range(1, remainingCapacity + 1):
                if coinValue <= j:
                    ways = (self.dp[i - 1][j] + self.dp[i][j - coinValue]) % self.MOD
                else:
                    ways = self.dp[i - 1][j]

                self.dp[i][j] = ways

        return self.dp[-1][-1]


if __name__ == "__main__":
    testCases = [([1, 2, 3], 4, 4), ([10], 10, 1)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
