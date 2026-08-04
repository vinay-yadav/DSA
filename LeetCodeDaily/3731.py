"""
Find Missing Elements
"""


class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        smallest, largest = min(nums), max(nums)
        num_set = set(nums)
        return [num for num in range(smallest, largest + 1) if num not in num_set]


if __name__ == "__main__":
    testCases = [
        ([1, 4, 2, 5], [3]),
        ([7, 8, 6, 9], []),
        ([5, 1], [2, 3, 4]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findMissingElements(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
