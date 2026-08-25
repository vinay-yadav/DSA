"""
Range Sum Query - Immutable
"""


class NumArray:
    def __init__(self, nums: list[int]):
        n = len(nums)

        self.nums = nums[:]
        for idx in range(1, n):
            self.nums[idx] = self.nums[idx] + self.nums[idx - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]

        return self.nums[right] - self.nums[left - 1]


if __name__ == "__main__":
    obj = NumArray([1, 3, 5])
    print(obj.sumRange(0, 2))
