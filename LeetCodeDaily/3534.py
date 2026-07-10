"""
Path Existence Queries in a Graph II
"""

import math
from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:

        nodePair = list()
        for i in range(n):
            nodePair.append((nums[i], i))

        nodePair.sort()

        nodeToIdx = [-1] * n
        for i in range(n):
            _, node = nodePair[i]
            nodeToIdx[node] = i

        rows, cols = n, int(math.log2(n) + 1)

        ancestorTable = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(n):
            farthestIdxOneHop = self.customUpperBound(
                nodePair, nodePair[i][0] + maxDiff
            )
            ancestorTable[i][0] = farthestIdxOneHop

        for j in range(1, cols):
            for node in range(n):
                ancestorTable[node][j] = ancestorTable[ancestorTable[node][j - 1]][
                    j - 1
                ]

        result = [-1] * len(queries)

        for idx, (u, v) in enumerate(queries):
            a, b = nodeToIdx[u], nodeToIdx[v]

            if a == b:
                result[idx] = 0
                continue

            if a > b:
                a, b = b, a

            curr, jumps = a, 0

            for j in range(cols - 1, -1, -1):
                if ancestorTable[curr][j] < b:
                    curr = ancestorTable[curr][j]
                    jumps += 1 << j

            if ancestorTable[curr][0] >= b:
                result[idx] = jumps + 1

        return result

    def customUpperBound(self, arr, target):
        n = len(arr)
        left, right = 0, n - 1
        result = 0

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid][0] <= target:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result


if __name__ == "__main__":
    testCases = [
        (5, [1, 8, 3, 4, 2], 3, [[0, 3], [2, 4]], [1, 1]),
        (5, [5, 3, 1, 9, 10], 2, [[0, 1], [0, 2], [2, 3], [4, 3]], [1, 2, -1, 1]),
        (3, [3, 6, 1], 1, [[0, 0], [0, 1], [1, 2]], [0, -1, -1]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().pathExistenceQueries(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
