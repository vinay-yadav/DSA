"""
Minimum Swaps to Sort by Digit Sum
"""


class Solution:
    """
    T.C: O(nlogn)
    S.C: O(n)
    """

    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(num):
            s = 0
            while num > 0:
                num, d = divmod(num, 10)
                s += d

            return s

        curPos = {}
        for idx, num in enumerate(nums):
            curPos[num] = idx

        sortedNums = sorted(nums, key=lambda x: (digit_sum(x), x))

        swaps = 0
        for idx, num in enumerate(sortedNums):
            if nums[idx] == num:
                continue

            pos = curPos[num]
            nums[idx], nums[pos] = nums[pos], nums[idx]

            curPos[nums[pos]] = pos

            swaps += 1

        return swaps

    def minSwaps1(self, nums: list[int]) -> int:
        n = len(nums)
        digitSum = []

        for idx in range(n):
            num = nums[idx]
            s = 0

            while num > 0:
                num, digit = divmod(num, 10)
                s += digit

            digitSum.append(s)

        curPos = {}
        for idx, num in enumerate(nums):
            curPos[num] = idx

        ds = sorted(zip(digitSum, nums))
        ds.sort()

        swaps = 0
        for idx, (_, num) in enumerate(ds):
            if nums[idx] == num:
                continue

            pos = curPos[num]
            nums[idx], nums[pos] = nums[pos], nums[idx]

            curPos[nums[pos]] = pos

            swaps += 1

        return swaps


if __name__ == "__main__":
    testCases = [
        ([37, 100], 1),
        ([22, 14, 33, 7], 0),
        ([18, 43, 34, 16], 2),
        ([17, 2, 90, 38], 1),
        ([3, 1, 2], 2),
        ([2, 1, 4, 3], 2),
        ([2, 3, 4, 1], 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minSwaps(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
