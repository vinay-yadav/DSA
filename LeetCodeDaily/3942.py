"""
Minimum Operations to Sort a Permutation
"""


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        asc_count = dsc_count = 0

        for idx in range(1, n):
            asc_count += nums[idx] == (nums[idx - 1] + 1) % n
            dsc_count += nums[idx - 1] == (nums[idx] + 1) % n

        if asc_count == n - 1:
            if nums[0] == 0:
                return 0

            left_rot = n - nums[0]
            right_rot = 1 + (nums[-1] + 1) + 1

            return min(left_rot, right_rot)

        if dsc_count == n - 1:
            left_rot = n - nums[-1] + 1
            right_rot = (nums[0] + 1) % n + 1

            return min(left_rot, right_rot)

        return -1


if __name__ == "__main__":
    testCases = [
        ([0, 2, 1], 2),
        ([1, 0, 2], 2),
        ([2, 0, 1, 3], -1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minOperations(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
