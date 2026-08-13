"""
Length of Longest Subarray With at Most K Frequenct
"""

from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)

        i = j = longest_subarray = 0
        while j < n:
            freq[nums[j]] += 1

            while i < j and freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1

            longest_subarray = max(longest_subarray, j - i + 1)
            j += 1

        return longest_subarray

    def maxSubarrayLength1(self, nums: list[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)

        longest_subarray = 0

        i = j = 0
        while j < n:
            curr = nums[j]

            if freq[curr] + 1 <= k:
                freq[curr] += 1
                longest_subarray = max(longest_subarray, j - i + 1)
                j += 1
            else:
                freq[nums[i]] -= 1
                i += 1

        return longest_subarray


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3, 1, 2, 3, 1, 2], 2, 6),
        ([1, 2, 1, 2, 1, 2, 1, 2], 1, 2),
        ([1, 1, 1, 3], 2, 3),
        ([2, 2, 1, 2], 1, 2),
        ([1, 1, 3, 3], 1, 2),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxSubarrayLength(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
