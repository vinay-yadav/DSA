"""
Longest Substring of One Repeating Character
"""


class Node:
    def __init__(self, pre=0, suf=0, maxLen=0, leftChar="", rightChar="") -> None:
        self.pre = pre
        self.suf = suf
        self.maxLen = maxLen
        self.leftChar = leftChar
        self.rightChar = rightChar


class SegmentTree:
    def __init__(self, s) -> None:
        self.segmentTree = [Node()] * 4 * len(s)
        self.s = s

    def merge(
        self, leftNode: Node, rightNode: Node, leftSize: int, rightSize: int
    ) -> Node:
        res = Node()

        res.leftChar = leftNode.leftChar
        res.rightChar = rightNode.rightChar

        res.pre = leftNode.pre
        if leftNode.pre == leftSize and leftNode.rightChar == rightNode.leftChar:
            res.pre += rightNode.pre

        res.suf = rightNode.suf
        if rightNode.suf == rightSize and leftNode.rightChar == rightNode.leftChar:
            res.suf += leftNode.suf

        res.maxLen = max(leftNode.maxLen, rightNode.maxLen)
        if leftNode.rightChar == rightNode.leftChar:
            res.maxLen = max(res.maxLen, leftNode.suf + rightNode.pre)

        return res

    def buildSegmentTree(self, idx, low, high):
        if low == high:
            self.segmentTree[idx] = Node(1, 1, 1, self.s[low], self.s[low])
            return

        left = 2 * idx + 1
        right = 2 * idx + 2

        mid = low + (high - low) // 2

        self.buildSegmentTree(left, low, mid)
        self.buildSegmentTree(right, mid + 1, high)

        self.segmentTree[idx] = self.merge(
            self.segmentTree[left], self.segmentTree[right], mid - low + 1, high - mid
        )

    def update(self, idx, low, high, position, ch):
        if low == high:
            self.segmentTree[idx] = Node(1, 1, 1, ch, ch)
            return

        left = 2 * idx + 1
        right = 2 * idx + 2

        mid = low + (high - low) // 2

        if position <= mid:
            self.update(left, low, mid, position, ch)
        else:
            self.update(right, mid + 1, high, position, ch)

        self.segmentTree[idx] = self.merge(
            self.segmentTree[left], self.segmentTree[right], mid - low + 1, high - mid
        )


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: list[int]
    ) -> list[int]:
        n = len(s)

        st = SegmentTree(s)
        st.buildSegmentTree(0, 0, n - 1)

        result = []
        for i in range(len(queryCharacters)):
            pos = queryIndices[i]
            ch = queryCharacters[i]

            st.update(0, 0, n - 1, pos, ch)

            result.append(st.segmentTree[0].maxLen)

        return result


if __name__ == "__main__":
    testCases = [
        ("babacc", "bcb", [1, 3, 3], [3, 3, 4]),
        ("abyzz", "aa", [2, 1], [2, 3]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().longestRepeating(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
