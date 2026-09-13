"""
Count Values With Equally Spaced Occurrences I
"""

from collections import defaultdict


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq = defaultdict(list)
        for idx, num in enumerate(nums):
            freq[num].append(idx)

        result = 0
        for value in freq.values():
            if len(value) == 3 and value[1] - value[0] == value[2] - value[1]:
                result += 1

        return result


if __name__ == "__main__":
    testCases = [
        ([1, 8, 1, 5, 1, 5, 8, 5], 2),
        ([8, 8, 8, 8], 0),
        ([8, 6, 6, 8, 8], 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countSpecialIntegers(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
