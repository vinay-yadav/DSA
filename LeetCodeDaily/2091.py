"""
Removing Minimum and Maximum From Array
"""


class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)

        if n < 2:
            return 1

        minEle, maxEle = float("inf"), float("-inf")
        minIndex = maxIndex = -1

        for idx, num in enumerate(nums):
            if num < minEle:
                minIndex = idx
                minEle = num

            if num > maxEle:
                maxIndex = idx
                maxEle = num

        left, right = min(minIndex, maxIndex), max(minIndex, maxIndex)

        return min(
            right + 1,                  # delete from left
            n - left,                   # delete from right
            (left + 1) + (n - right)    # delete one from left and one from right
        )


if __name__ == "__main__":
    testCases = [
        ([101], 1),
        ([2, 10, 7, 5, 4, 1, 8, 6], 5),
        ([0, -4, 19, 1, 8, -2, -3, 5], 3),
        ([0, 1, 8, -2, -3, 5, -4, 19], 2),
        ([10, 9, 8, 7, -100, 1000, 6, 5, 4, 3], 6),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minimumDeletions(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
