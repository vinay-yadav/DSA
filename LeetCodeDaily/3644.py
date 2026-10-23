"""
Maximum K to Sort a Permutation
"""


class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        k = -1  # "11111111" (all bits set)

        for idx, num in enumerate(nums):
            if idx != num:
                k &= num

        return 0 if k == -1 else k


if __name__ == "__main__":
    testCases = [
        ([0, 3, 2, 1], 1),
        ([0, 1, 3, 2], 2),
        ([3, 2, 1, 0], 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().sortPermutation(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
