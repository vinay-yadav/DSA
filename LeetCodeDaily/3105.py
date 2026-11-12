"""
Longest Strictly Increasing or Strictly Decreasing Subarray
"""


class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        longest = inc = dec = 1

        for j in range(1, len(nums)):
            if nums[j] > nums[j - 1]:
                inc += 1
                dec = 1
            elif nums[j] < nums[j - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1

            longest = max(longest, inc, dec)

        return longest

    def longestMonotonicSubarray2(self, nums: list[int]) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        n = len(nums)
        longest_subarray = 1

        if n < 2:
            return longest_subarray

        # strictly increasing
        i, j = 0, 1
        while j < n:
            if nums[j] > nums[j - 1]:
                longest_subarray = max(longest_subarray, j - i + 1)
            else:
                i = j

            j += 1

        # strictly decreasing
        i, j = 0, 1
        while j < n:
            if nums[j] < nums[j - 1]:
                longest_subarray = max(longest_subarray, j - i + 1)
            else:
                i = j

            j += 1

        return longest_subarray

    def longestMonotonicSubarray1(self, nums: list[int]) -> int:
        """
        Brute Force
        TC: O(n^3)
        SC: O(1)
        """
        n = len(nums)
        longest_subarray = 1

        for i in range(n):
            for j in range(i + 1, n):
                is_strictly_increasing = is_strictly_decreasing = True

                for x in range(i, j):
                    if not nums[x] < nums[x + 1]:
                        is_strictly_increasing = False
                        break

                for x in range(i, j):
                    if not nums[x] > nums[x + 1]:
                        is_strictly_decreasing = False
                        break

                if is_strictly_increasing or is_strictly_decreasing:
                    longest_subarray = max(longest_subarray, j - i + 1)

        return longest_subarray


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3, 2, 1], 3),
        ([1, 4, 3, 3, 2], 2),
        ([3, 3, 3, 3], 1),
        ([3, 2, 1], 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().longestMonotonicSubarray(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
