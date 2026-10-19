"""
Find Target Indices After Sorting Array
"""


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        """
        TC: O(n)
        SC: O(1)
        """
        less_than_target = 0
        target_count = 0

        for num in nums:
            if num < target:
                less_than_target += 1
            elif num == target:
                target_count += 1

        result = []
        count = less_than_target
        while count < target_count + less_than_target:
            result.append(count)
            count += 1

        return result

    def targetIndices1(self, nums: list[int], target: int) -> list[int]:
        """
        TC: O(nlogn)
        SC: O(1)
        """
        result = []

        nums.sort()

        for idx, num in enumerate(nums):
            if num == target:
                result.append(idx)

        return result


if __name__ == "__main__":
    testCases = [
        ([1, 2, 5, 2, 3], 2, [1, 2]),
        ([1, 2, 5, 2, 3], 3, [3]),
        ([1, 2, 5, 2, 3], 5, [4]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().targetIndices(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
