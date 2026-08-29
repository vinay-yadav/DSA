"""
Make Lexicographically Smallest Array by Swapping Elements
"""

from collections import defaultdict, deque


class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)

        if n < 2:
            return nums

        sortedNums = sorted(nums[:])

        groupNum = 0
        groupToList = defaultdict(deque)
        groupToList[groupNum].append(sortedNums[0])

        numToGroup = defaultdict(int)
        numToGroup[sortedNums[0]] = groupNum

        for i in range(1, n):
            if abs(sortedNums[i] - sortedNums[i - 1]) > limit:
                groupNum += 1

            groupToList[groupNum].append(sortedNums[i])
            numToGroup[sortedNums[i]] = groupNum

        if len(groupToList) == 1:
            return sortedNums

        for idx, num in enumerate(nums):
            group = numToGroup[num]
            nums[idx] = groupToList[group].popleft()

        return nums


if __name__ == "__main__":
    testCases = [
        ([3, 1, 2], 1, [1, 2, 3]),
        ([1, 5, 3, 9, 8], 2, [1, 3, 5, 8, 9]),
        ([1, 7, 6, 18, 2, 1], 3, [1, 6, 7, 18, 1, 2]),
        ([1, 7, 28, 19, 10], 3, [1, 7, 28, 19, 10]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().lexicographicallySmallestArray(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
