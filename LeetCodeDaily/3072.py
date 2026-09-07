"""
Distribute Elements Into Two Arrays II
"""


class SegmentTree:
    def __init__(self, arraySize) -> None:
        self.size = arraySize
        self.segTree = [0] * 4 * arraySize

    def update(self, newValue):
        self.updateSegmentTree(0, 0, self.size - 1, newValue)

    def updateSegmentTree(self, idx, low, high, newValue):
        if low == high:
            self.segTree[idx] += 1
            return

        mid = low + (high - low) // 2
        left, right = 2 * idx + 1, 2 * idx + 2

        if newValue <= mid:
            self.updateSegmentTree(left, low, mid, newValue)
        else:
            self.updateSegmentTree(right, mid + 1, high, newValue)

        self.segTree[idx] = self.segTree[left] + self.segTree[right]

    def query(self, start, end) -> int:
        return self.rangeQuery(start, end, 0, 0, self.size - 1)

    def rangeQuery(self, start, end, idx, low, high) -> int:
        if low > end or high < start:
            return 0

        if low >= start and high <= end:
            return self.segTree[idx]

        mid = low + (high - low) // 2
        left, right = 2 * idx + 1, 2 * idx + 2

        return self.rangeQuery(start, end, left, low, mid) + self.rangeQuery(
            start, end, right, mid + 1, high
        )


class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        sortedNums = sorted(nums[::])

        compressedValue = 0
        compressedNumMap = {}

        for num in sortedNums:
            if num in compressedNumMap:
                continue

            compressedNumMap[num] = compressedValue
            compressedValue += 1

        segmentTree1 = SegmentTree(compressedValue)
        segmentTree2 = SegmentTree(compressedValue)

        nums1, nums2 = [nums[0]], [nums[1]]
        segmentTree1.update(compressedNumMap[nums[0]])
        segmentTree2.update(compressedNumMap[nums[1]])

        for i in range(2, n):
            newElement = nums[i]
            cv = compressedNumMap[newElement]

            count1 = segmentTree1.query(cv + 1, compressedValue)
            count2 = segmentTree2.query(cv + 1, compressedValue)

            addToNums1 = False

            if count1 > count2:
                addToNums1 = True
            elif count1 == count2:
                addToNums1 = len(nums1) <= len(nums2)

            if addToNums1:
                nums1.append(newElement)
                segmentTree1.update(cv)
            else:
                nums2.append(newElement)
                segmentTree2.update(cv)

        nums1.extend(nums2)
        return nums1


if __name__ == "__main__":
    testCases = [
        ([2, 1, 3, 3], [2, 3, 1, 3]),
        ([5, 14, 3, 1, 2], [5, 3, 1, 2, 14]),
        ([3, 3, 3, 3], [3, 3, 3, 3]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().resultArray(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
