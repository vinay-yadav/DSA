"""
Count Good Cyclic Rotations
"""


class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n // 2

        first_half_sum = 0
        for i in range(half):
            first_half_sum += nums[i]

        second_half_sum = 0
        for i in range(half, n):
            second_half_sum += nums[i]

        result = 0

        i, j = 0, half
        while j < n:
            first_half_sum = first_half_sum - nums[i] + nums[j]
            second_half_sum = second_half_sum - nums[j] + nums[i]

            if first_half_sum != second_half_sum:
                result += 1

            i += 1
            j += 1

        return result


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3, 4, 5, 6], 3),
        ([1, 2, 1, 2], 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countGoodRotations(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
