"""
Predict the Winner
"""


class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)

        dp = [[float("-inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        def func(i, j) -> int:
            if dp[i][j] != float("-inf"):
                return dp[i][j]

            dp[i][j] = max(
                nums[i] - func(i + 1, j),
                nums[j] - func(i, j - 1),
            )

            return dp[i][j]

        return func(0, n - 1) >= 0


if __name__ == "__main__":
    testCases = [
        ([1, 5, 2], False),
        ([1, 5, 233, 7], True),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().predictTheWinner(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
