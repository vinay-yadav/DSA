"""
Smallest Index With Digit Sum Equal to Index
"""


class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for idx, num in enumerate(nums):
            digitSum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                digitSum += digit

            if digitSum == idx:
                return idx

        return -1


if __name__ == "__main__":
    testCases = [
        ([1, 3, 2], 2),
        ([1, 10, 11], 1),
        ([1, 2, 3], -1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().smallestIndex(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
