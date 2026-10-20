"""
Sum of Sortable Integers
"""

from Algorithms.PatternMatching.kmp import KMP


class Solution:
    def __init__(self):
        self.kmp = KMP()

    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        result = 0
        for k in range(1, n + 1):
            if n % k != 0:
                continue

            rotation_possible = True
            for start in range(0, n, k):
                partitioned_nums = nums[start : start + k]
                partitioned_sorted_nums = sorted_nums[start : start + k]

                if not self.is_rotation_possible(
                    partitioned_nums, partitioned_sorted_nums
                ):
                    rotation_possible = False
                    break

            if rotation_possible:
                result += k

        return result

    def is_rotation_possible(self, nums, sorted_nums):
        text = sorted_nums + sorted_nums
        pattern = nums

        return self.kmp.search(text, pattern) >= 0


if __name__ == "__main__":
    testCases = [
        ([3, 1, 2], 3),
        ([7, 6, 5], 0),
        ([5, 8], 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().sortableIntegers(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
