"""
Maximum Alternating Sum of Squares
"""


class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums = [num * num for num in nums]
        nums.sort()

        result = 0

        i, j = 0, len(nums) - 1
        while i < j:
            result += nums[j]
            result -= nums[i]

            i += 1
            j -= 1

        if i == j:
            result += nums[i]

        return result


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3], 12),
        ([1, -1, 2, -2, 3, -3], 16),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxAlternatingSum(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
