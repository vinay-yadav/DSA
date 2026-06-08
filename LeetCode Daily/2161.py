"""
2161. Partition Array According to Given Pivot
"""

from typing import List, Optional, Tuple


class Solution:
    def pivotArray1(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)

        numLessThanPivot, numsGreaterThanPivot = [], []
        pivotCount = 0

        for i in range(n):
            if nums[i] < pivot:
                numLessThanPivot.append(nums[i])

            if nums[i] > pivot:
                numsGreaterThanPivot.append(nums[i])

            if nums[i] == pivot:
                pivotCount += 1

        return numLessThanPivot + [pivot] * pivotCount + numsGreaterThanPivot

    def pivotArray2(self, nums: List[int], pivot: int) -> List[Optional[int]]:
        ans: List[Optional[int]] = [None] * len(nums)

        numLessThanPivot = pivotCount = 0

        for num in nums:
            if num == pivot:
                pivotCount += 1
            elif num < pivot:
                numLessThanPivot += 1

        i, j, k = 0, numLessThanPivot, numLessThanPivot + pivotCount
        for num in nums:
            if num < pivot:
                ans[i] = num
                i += 1
            elif num == pivot:
                ans[j] = num
                j += 1
            else:
                ans[k] = num
                k += 1

        return ans


if __name__ == "__main__":
    testCases: List[Tuple[List, int, List]] = [
        ([9, 12, 5, 10, 14, 3, 10], 10, [9, 5, 3, 10, 10, 12, 14]),
        ([-3, 4, 3, 2], 2, [-3, 2, 4, 3]),
    ]

    for idx, (nums, pivot, expected) in enumerate(testCases):
        result = Solution().pivotArray2(nums, pivot)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
