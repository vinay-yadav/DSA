"""
Max Sum Non-Adjacent Elements
"""


class Solution:
    def solve(self, arr):
        n = len(arr)
        self.dp = [-1] * (n + 1)

        return self.topDown(arr, n - 1)
        # return self.bottomUp(arr)

    def topDown(self, arr, position):
        if position < 0:
            return 0

        if self.dp[position] != -1:
            return self.dp[position]

        self.dp[position] = (
            res := max(
                arr[position] + self.topDown(arr, position - 2),
                self.topDown(arr, position - 1),
            )
        )
        return res

    def bottomUp(self, arr):
        self.dp = [-1] * len(arr)
        self.dp[0] = arr[0]
        self.dp[1] = max(arr[0], arr[1])

        for i in range(2, len(arr)):
            self.dp[i] = max(self.dp[i - 1], arr[i] + self.dp[i - 2])

        return self.dp[-1]


if __name__ == "__main__":
    testCases = [([4, 3, 8, 5, 3, 8], 20), ([1, 100, 5, 1, 10, 6], 110)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
