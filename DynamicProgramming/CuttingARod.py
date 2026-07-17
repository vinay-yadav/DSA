"""
Cutting a Rod
"""


class Solution:
    def solve(self, A):
        n = len(A)
        self.dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            self.dp[i][0] = self.dp[0][i] = 0

        return self.topDown(n, n, A)

    def topDown(self, cutSize, rodSize, arr):
        if self.dp[cutSize][rodSize] != -1:
            return self.dp[cutSize][rodSize]

        if cutSize <= rodSize:
            self.dp[cutSize][rodSize] = max(
                self.topDown(cutSize - 1, rodSize, arr),
                self.topDown(cutSize, rodSize - cutSize, arr) + arr[cutSize - 1],
            )
        else:
            self.dp[cutSize][rodSize] = self.topDown(cutSize - 1, rodSize, arr)

        return self.dp[cutSize][rodSize]


if __name__ == "__main__":
    testCases = [([1, 5, 2, 5, 6], 11), ([3, 4, 1, 6, 2], 15)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
