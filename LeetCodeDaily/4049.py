"""
Count Values With Equally Spaced Occurrences II
"""

from collections import defaultdict


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        result = 0

        last_seen = {}
        diff = defaultdict(list)
        for idx, num in enumerate(nums):
            if num in last_seen:
                diff[num].append(idx - last_seen[num])
            last_seen[num] = idx

        for values in diff.values():
            val_len = len(values)
            if val_len < 2:
                continue

            if len(set(values)) == 1:
                result += 1

        return result


if __name__ == "__main__":
    testCases = [
        ([1, 8, 1, 5, 1, 5, 8, 5], 2),
        ([8, 8, 8, 8], 1),
        ([8, 6, 6, 8, 8], 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countSpecialIntegers(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
