"""
Sum of Squares of Special Elements
"""


class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        result = 0

        for idx, num in enumerate(nums):
            if n % (idx + 1) == 0:
                result += num * num

        return result


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3, 4], 21),
        ([2, 7, 1, 19, 18, 3], 63),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().sumOfSquares(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
