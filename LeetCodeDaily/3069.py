"""
Distribute Elements Into Two Arrays I
"""


class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr1, arr2 = [nums[0]], [nums[1]]

        for i in range(2, n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        arr1.extend(arr2)

        return arr1


if __name__ == "__main__":
    testCases = [
        ([2, 1, 3], [2, 3, 1]),
        ([5, 4, 3, 8], [5, 3, 4, 8]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().resultArray(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
