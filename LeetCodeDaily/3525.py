"""
Find X Value of Array II
"""


class Node:
    __slots__ = ("cnt", "prod")

    def __init__(self, k: int) -> None:
        self.cnt = [0] * k
        self.prod = 0


class SegmentTree:
    def __init__(self, nums: list[int], k: int) -> None:
        self.k = k
        self.n = len(nums)
        self.segTree = [Node(k) for _ in range(4 * self.n)]
        self.build(0, 0, self.n - 1, nums)

    def build(self, i: int, l: int, r: int, nums: list[int]) -> None:
        if l == r:
            self.leafNode(i, nums[l])
            return

        mid = l + (r - l) // 2
        self.build(2 * i + 1, l, mid, nums)
        self.build(2 * i + 2, mid + 1, r, nums)
        self.segTree[i] = self.mergeNodes(
            self.segTree[2 * i + 1], self.segTree[2 * i + 2]
        )

    def leafNode(self, i: int, value: int) -> None:
        node = self.segTree[i]
        for x in range(self.k):
            node.cnt[x] = 0

        r = value % self.k
        node.cnt[r] = 1
        node.prod = r

    def mergeNodes(self, left: Node, right: Node) -> Node:
        result = Node(self.k)
        result.prod = (left.prod * right.prod) % self.k

        for x in range(self.k):
            result.cnt[x] = left.cnt[x]
        for x in range(self.k):
            newRem = (left.prod * x) % self.k
            result.cnt[newRem] += right.cnt[x]

        return result

    def update(self, index: int, value: int) -> None:
        self.segTreeUpdate(0, 0, self.n - 1, index, value)

    def segTreeUpdate(self, i: int, l: int, r: int, index: int, value: int) -> None:
        if l == r:
            self.leafNode(i, value)
            return

        mid = l + (r - l) // 2
        if index <= mid:
            self.segTreeUpdate(2 * i + 1, l, mid, index, value)
        else:
            self.segTreeUpdate(2 * i + 2, mid + 1, r, index, value)

        self.segTree[i] = self.mergeNodes(
            self.segTree[2 * i + 1], self.segTree[2 * i + 2]
        )

    def query(self, start: int, end: int) -> Node:
        return self.segTreeQuery(start, end, 0, 0, self.n - 1)

    def segTreeQuery(self, start: int, end: int, i: int, l: int, r: int) -> Node:
        if l >= start and r <= end:
            return self.segTree[i]

        mid = l + (r - l) // 2
        if end <= mid:
            return self.segTreeQuery(start, end, 2 * i + 1, l, mid)
        if start > mid:
            return self.segTreeQuery(start, end, 2 * i + 2, mid + 1, r)

        left = self.segTreeQuery(start, end, 2 * i + 1, l, mid)
        right = self.segTreeQuery(start, end, 2 * i + 2, mid + 1, r)
        return self.mergeNodes(left, right)


class Solution:
    def resultArray(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[int]:
        n = len(nums)
        segTree = SegmentTree(nums, k)
        result = []

        for index, value, start, x in queries:
            segTree.update(index, value)
            node = segTree.query(start, n - 1)
            result.append(node.cnt[x])

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
