"""
Range Sum Query - Mutable
"""


class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.size = len(nums)
        self.segmentTree = [0] * (4 * self.size)
        self.buildSegmentTee(0, 0, self.size - 1)

    def buildSegmentTee(self, idx, low, high):
        if low == high:
            self.segmentTree[idx] = self.nums[low]
            return

        mid = low + (high - low) // 2
        left, right = 2 * idx + 1, 2 * idx + 2

        self.buildSegmentTee(left, low, mid)
        self.buildSegmentTee(right, mid + 1, high)

        self.segmentTree[idx] = self.segmentTree[left] + self.segmentTree[right]

    def update(self, index: int, val: int) -> None:
        self.updateSegmentTree(0, 0, self.size - 1, index, val)

    def updateSegmentTree(self, idx, low, high, positoin, value):
        if low == high:
            self.segmentTree[idx] = value
            return

        mid = low + (high - low) // 2

        if positoin <= mid:
            self.updateSegmentTree(2 * idx + 1, low, mid, positoin, value)
        else:
            self.updateSegmentTree(2 * idx + 2, mid + 1, high, positoin, value)

        self.segmentTree[idx] = (
            self.segmentTree[2 * idx + 1] + self.segmentTree[2 * idx + 2]
        )

    def sumRange(self, left: int, right: int) -> int:
        return self.findRangeSum(left, right, 0, 0, self.size - 1)

    def findRangeSum(self, start, end, idx, low, high) -> int:
        if low > end or high < start:
            return 0

        if low >= start and high <= end:
            return self.segmentTree[idx]

        mid = low + (high - low) // 2
        left, right = 2 * idx + 1, 2 * idx + 2

        return self.findRangeSum(start, end, left, low, mid) + self.findRangeSum(
            start, end, right, mid + 1, high
        )


if __name__ == "__main__":
    obj = NumArray([1, 3, 5])
    print(obj.sumRange(1, 2))
    obj.update(1, 2)
    print(obj.sumRange(0, 2))
