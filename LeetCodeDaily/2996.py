"""
Smallest Missing Integer Greater Than Sequential Prefix Sum
"""


class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        n = len(nums)
        count = [0] * 1276

        for num in nums:
            count[num] += 1

        largest_sequential_sum = nums[0]
        j = 1
        while j < n and nums[j] == nums[j - 1] + 1:
            largest_sequential_sum += nums[j]
            j += 1

        while count[largest_sequential_sum] != 0:
            largest_sequential_sum += 1

        return largest_sequential_sum


if __name__ == "__main__":
    testCases = [
        ([5], 6),
        ([1, 2, 3, 2, 5], 6),
        ([1, 2, 3, 2, 5, 6], 7),
        ([3, 4, 5, 1, 12, 14, 13], 15),
        ([29, 30, 31, 32, 33, 34, 35, 36, 37], 297),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().missingInteger(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
