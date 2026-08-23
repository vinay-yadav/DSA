"""
Subsets II
"""

from collections import defaultdict


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        unique_nums = list(count.keys())  # list so we can index by position

        def backtrack(start, temp_list):
            # every prefix (including empty) is a valid subset
            result.append(temp_list.copy())

            for i in range(start, len(unique_nums)):
                key = unique_nums[i]
                available = count[key]

                # try including this key 1, 2, ..., available times
                for _ in range(1, available + 1):
                    temp_list.append(key)
                    backtrack(i + 1, temp_list)

                # undo all the appends for this key before moving to next i
                for _ in range(available):
                    temp_list.pop()

        backtrack(0, [])

        return result


if __name__ == "__main__":
    testCases = [
        ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
        ([0], [[], [0]]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().subsetsWithDup(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
