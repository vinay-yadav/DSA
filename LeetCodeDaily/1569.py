"""
Number of Ways to Reorder Array to Get Same BST
"""


class Solution:
    MOD = 1_000_000_007

    def numOfWays(self, nums: list[int]) -> int:
        n = len(nums)
        PT = [[] for _ in range(n + 1)]

        for i in range(n):
            PT[i] = [1] * (i + 1)
            for j in range(1, i):
                PT[i][j] = (PT[i - 1][j - 1] + PT[i - 1][j]) % self.MOD

        def solve(arr):
            length = len(arr)

            if length < 3:
                return 1

            left_arr, right_arr = [], []
            for idx in range(1, length):
                if arr[idx] < arr[0]:
                    left_arr.append(arr[idx])
                else:
                    right_arr.append(arr[idx])

            x = solve(left_arr) % self.MOD
            y = solve(right_arr) % self.MOD
            z = PT[length - 1][len(left_arr)]

            return ((x * y) % self.MOD * z) % self.MOD

        return (solve(nums) - 1) % self.MOD


if __name__ == "__main__":
    testCases = [
        ([2, 1, 3], 1),
        ([3, 4, 5, 1, 2], 5),
        ([1, 2, 3], 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().numOfWays(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
