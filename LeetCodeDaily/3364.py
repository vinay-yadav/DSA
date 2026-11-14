"""
Minimum Positive Sum Subarray
"""


class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        """
        Brute Force
        TC: O(n^2)
        SC: O(1)
        """
        n = len(nums)
        min_sum = float("inf")

        for i in range(n):
            subarray_sum = 0
            for j in range(i, n):
                subarray_length = j - i + 1
                subarray_sum += nums[j]

                if subarray_length > r:
                    break

                if subarray_length < l or subarray_sum <= 0:
                    continue

                min_sum = min(min_sum, subarray_sum)

        return -1 if min_sum == float("inf") else int(min_sum)


if __name__ == "__main__":
    testCases = [
        ([3, -2, 1, 4], 2, 3, 1),
        ([-2, 2, -3, 1], 2, 3, -1),
        ([1, 2, 3, 4], 2, 4, 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minimumSumSubarray(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
