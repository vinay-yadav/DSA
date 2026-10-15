"""
Subarrays Distinct Element Sum of Squares I
"""


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            temp_set = set()
            for j in range(i, n):
                num = nums[j]
                temp_set.add(num)
                result += len(temp_set) * len(temp_set)

        return result


if __name__ == "__main__":
    testCases = [
        ([1, 2, 1], 15),
        ([1, 1], 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().sumCounts(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
