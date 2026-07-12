"""
Rank Transform of an Array
"""

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = arr[:]
        nums.sort()

        rankDict = dict()
        rank = 1

        for num in nums:
            if num in rankDict:
                continue

            rankDict[num] = rank
            rank += 1

        for i in range(len(arr)):
            arr[i] = rankDict[arr[i]]

        return arr


if __name__ == "__main__":
    testCases = [
        ([40, 10, 20, 30], [4, 1, 2, 3]),
        ([100, 100, 100], [1, 1, 1]),
        ([37, 12, 28, 9, 100, 56, 80, 5, 12], [5, 3, 4, 2, 8, 6, 7, 1, 3]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().arrayRankTransform(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
