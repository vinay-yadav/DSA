"""
Subarray Product Less Than K
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        n = len(nums)

        valid_subarray_count = i = j = 0

        product = 1
        while j < n:
            product *= nums[j]

            while i <= j and product >= k:
                product //= nums[i]
                i += 1

            valid_subarray_count += j - i + 1
            j += 1

        return valid_subarray_count


if __name__ == "__main__":
    testCases = [
        ([10, 5, 2, 6], 100, 8),
        ([1, 2, 3], 0, 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().numSubarrayProductLessThanK(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
