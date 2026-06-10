"""
Maximum Total Subarray Value
"""

from typing import List, Tuple


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxNum = float("-inf")
        minNum = float("inf")

        for num in nums:
            if num > maxNum:
                maxNum = num

            if num < minNum:
                minNum = num

        return int((maxNum - minNum) * k)


if __name__ == "__main__":
    testCases: List[Tuple[List[int], int, int]] = [
        ([1, 3, 2], 2, 4),
        ([4, 2, 5, 1], 3, 12),
    ]

    for idx, (nums, pivot, expected) in enumerate(testCases):
        result = Solution().maxTotalValue(nums, pivot)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
