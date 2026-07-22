"""
Maximize Active Section with Trade II
"""


class SegmentTree:
    def __init__(self, arr) -> None:
        self.segmentTree = [0] * 4 * len(arr)
        self.arr = arr

    def constructSegmentTree(self):
        self.buildSegmentTree(0, 0, len(self.arr) - 1)
        return self.segmentTree

    def buildSegmentTree(self, idx, low, high):
        if low == high:
            self.segmentTree[idx] = self.arr[low]
            return

        left = 2 * idx + 1
        right = 2 * idx + 2

        mid = low + (high - low) // 2

        self.buildSegmentTree(left, low, mid)
        self.buildSegmentTree(right, mid + 1, high)

        self.segmentTree[idx] = max(self.segmentTree[left], self.segmentTree[right])

    def querySegmentTree(self, start, end, idx, low, high):
        if low > end or high < start:
            return float("-inf")

        if low >= start and high <= end:
            return self.segmentTree[idx]

        mid = low + (high - low) // 2

        return max(
            self.querySegmentTree(start, end, 2 * idx + 1, low, mid),
            self.querySegmentTree(start, end, 2 * idx + 2, mid + 1, high),
        )

    def RMQ(self, a, b):
        return self.querySegmentTree(a, b, 0, 0, len(self.arr) - 1)


class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: list[list[int]]
    ) -> list[int]:
        numOfOnes = s.count("1")
        n = len(s)

        blockStart = []
        blockEnd = []
        blockSize = []

        i = 0
        while i < n:
            if s[i] == "0":
                start = i

                while i < n and s[i] == "0":
                    i += 1

                blockStart.append(start)
                blockEnd.append(i - 1)
                blockSize.append((i - 1) - start + 1)
            else:
                i += 1

        if len(blockStart) < 2:
            return [numOfOnes] * len(queries)

        numOfBlocks = len(blockSize) - 1
        pairSum = []

        for i in range(numOfBlocks):
            pairSum.append(blockSize[i] + blockSize[i + 1])

        st = SegmentTree(pairSum)
        st.constructSegmentTree()

        result = []
        from bisect import bisect_left, bisect_right

        for li, ri in queries:
            low = bisect_left(blockEnd, li)
            high = bisect_right(blockStart, ri) - 1

            maxPairSum = 0
            if low < high:
                firstLen = blockEnd[low] - max(blockStart[low], li) + 1
                lastLen = min(blockEnd[high], ri) - blockStart[high] + 1

                if high - low == 1:
                    maxPairSum = firstLen + lastLen
                else:
                    pair1 = firstLen + blockSize[low + 1]
                    pair2 = lastLen + blockSize[high - 1]

                    RMQMaxPairSum = st.RMQ(low + 1, high - 2)

                    maxPairSum = max(pair1, pair2, RMQMaxPairSum)

            result.append(maxPairSum + numOfOnes)

        return result

    def naive(self, s: str, queries: list[list[int]]) -> list[int]:
        zeroPair = []
        numOfOnes = s.count("1")

        i, n = 0, len(s)
        while i < n:
            if s[i] == "0":
                start = i

                while i < n and s[i] == "0":
                    i += 1

                zeroPair.append((start, i - 1))
            else:
                i += 1

        print("zeroPair", zeroPair)

        result = []
        for low, high in queries:
            convertedZeroes = 0
            for i in range(len(zeroPair) - 1):
                a, b = zeroPair[i]
                c, d = zeroPair[i + 1]

                if low <= b and high >= c:
                    t1 = max(low, a)
                    t2 = min(high, d)

                    convertedZeroes += (b - t1 + 1) + (t2 - c + 1)
                    break

            result.append(convertedZeroes + numOfOnes)

        return result


if __name__ == "__main__":
    testCases = [
        ("01", [[0, 1]], [1]),
        ("0100", [[0, 3], [0, 2], [1, 3], [2, 3]], [4, 3, 1, 1]),
        ("1000100", [[1, 5], [0, 6], [0, 4]], [6, 7, 2]),
        ("01010", [[0, 3], [1, 4], [1, 3]], [4, 4, 2]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxActiveSectionsAfterTrade(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
