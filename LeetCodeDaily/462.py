"""
Minimum Moves to Equal Array Elements II
"""


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()

        mid_element = nums[n // 2]

        operations = 0
        for num in nums:
            operations += abs(num - mid_element)

        return operations


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3], 2),
        ([1, 10, 2, 9], 16),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minMoves2(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
