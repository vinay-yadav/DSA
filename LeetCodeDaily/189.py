"""
Rotate Array
"""


class Solution:
    def rotate(self, nums: list[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n > 1:
            if k > n:
                k = k % n

            self.reverseList(nums, 0, n - 1)
            self.reverseList(nums, 0, k - 1)
            self.reverseList(nums, k, n - 1)

        return nums

    def reverseList(self, nums, i, j):
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([1, 2], 7, [2, 1]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().rotate(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
