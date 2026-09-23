"""
Find X Value of Array II
"""


class Node:
    __slots__ = ("count", "product")

    def __init__(self, k) -> None:
        self.count = [0] * k
        self.product = 0


class SegmentTree:
    def __init__(self, nums, k) -> None:
        self.k = k
        self.nums = nums
        self.size = len(nums)
        self.segTree = [Node(k) for _ in range(4 * self.size)]

        self.buildSegmentTree(0, 0, self.size - 1)

    def buildSegmentTree(self, idx, low, high):
        if low == high:
            self.leafNode(idx, self.nums[low])
            return

        mid = low + (high - low) // 2
        left, right = self.getChildIndexes(idx)

        self.buildSegmentTree(left, low, mid)
        self.buildSegmentTree(right, mid + 1, high)

        self.segTree[idx] = self.mergeNodes(self.segTree[left], self.segTree[right])

    def leafNode(self, idx, value) -> None:
        for x in range(self.k):
            self.segTree[idx].count[x] = 0

        remainder = value % self.k
        self.segTree[idx].product = remainder
        self.segTree[idx].count[remainder] = 1

    def mergeNodes(self, leftNode: Node, rightNode: Node) -> Node:
        result = Node(self.k)
        result.product = (leftNode.product * rightNode.product) % self.k
        result.count = leftNode.count[:]

        for x in range(self.k):
            newRemainder = (leftNode.product * x) % self.k
            result.count[newRemainder] += rightNode.count[x]

        return result

    def update(self, idx, value):
        self.updateSegmentTree(0, 0, self.size - 1, idx, value)

    def updateSegmentTree(self, i, low, high, idx, value):
        if low == high:
            self.leafNode(i, value)
            return

        mid = low + (high - low) // 2
        left, right = self.getChildIndexes(i)

        if idx <= mid:
            self.updateSegmentTree(left, low, mid, idx, value)
        else:
            self.updateSegmentTree(right, mid + 1, high, idx, value)

        self.segTree[i] = self.mergeNodes(self.segTree[left], self.segTree[right])

    def query(self, start, end) -> Node:
        return self.querySegmentTree(start, end, 0, 0, self.size - 1)

    def querySegmentTree(self, start, end, idx, low, high) -> Node:
        if low >= start and high <= end:
            return self.segTree[idx]

        mid = low + (high - low) // 2
        left, right = self.getChildIndexes(idx)

        if end <= mid:
            return self.querySegmentTree(start, end, left, low, mid)

        if start > mid:
            return self.querySegmentTree(start, end, right, mid + 1, high)

        leftResult = self.querySegmentTree(start, end, left, low, mid)
        rightResult = self.querySegmentTree(start, end, right, mid + 1, high)

        return self.mergeNodes(leftResult, rightResult)

    @staticmethod
    def getChildIndexes(idx: int) -> tuple:
        index = 2 * idx
        return index + 1, index + 2


class Solution:
    def resultArray(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[int]:
        n = len(nums)
        result = []

        segTree = SegmentTree(nums, k)

        for index, value, start, x in queries:
            segTree.update(index, value)
            resultNode = segTree.query(start, n - 1)
            result.append(resultNode.count[x])

        return result


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3, 4, 5], 3, [[2, 2, 0, 2], [3, 3, 3, 0], [0, 1, 0, 1]], [2, 2, 2]),
        ([1, 2, 4, 8, 16, 32], 4, [[0, 2, 0, 2], [0, 2, 0, 1]], [1, 0]),
        ([1, 1, 2, 1, 1], 2, [[2, 1, 0, 1]], [5]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().resultArray(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
