"""
Minimum Score by Changing Two Elements
"""


class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()

        return min(
            nums[-3] - nums[0],
            nums[-1] - nums[2],
            nums[-2] - nums[1],
        )


if __name__ == "__main__":
    testCases = [
        ([1, 4, 7, 8, 5], 3),
        ([1, 4, 3], 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minimizeSum(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
