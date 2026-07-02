"""
Find the Safest Path in a Grid
"""

from collections import deque
from typing import List


class Solution:
    def __init__(self) -> None:
        self.n = 0
        self.directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        self.n = len(grid)

        """ Pre-calculation """
        queue = deque()
        visited = [[False] * self.n for _ in range(self.n)]
        distNearestTheif = [[0] * self.n for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited[i][j] = True

        level = 0
        while queue:
            queueSize = len(queue)

            for _ in range(queueSize):
                currI, currJ = queue.popleft()
                distNearestTheif[currI][currJ] = level

                for direct in self.directions:
                    newI = currI + direct[0]
                    newJ = currJ + direct[1]

                    if (
                        newI < 0
                        or newI >= self.n
                        or newJ < 0
                        or newJ >= self.n
                        or visited[newI][newJ]
                    ):
                        continue

                    queue.append((newI, newJ))
                    visited[newI][newJ] = True

            level += 1

        """ Apply Binary Search on SF """
        result = 0
        left, right = 0, max(max(row) for row in distNearestTheif)

        while left <= right:
            midSF = left + (right - left) // 2

            if self.check(distNearestTheif, midSF):
                result = midSF
                left = midSF + 1
            else:
                right = midSF - 1

        return result

    def check(self, thiefGrid, mid) -> bool:
        if thiefGrid[0][0] < mid:
            return False

        queue = deque()
        visited = [[False] * self.n for _ in range(self.n)]

        queue.append((0, 0))
        visited[0][0] = True

        while queue:
            i, j = queue.popleft()

            if i == self.n - 1 and j == self.n - 1:
                return True

            for direct in self.directions:
                p, q = i + direct[0], j + direct[1]

                if (
                    p >= 0
                    and p < self.n
                    and q >= 0
                    and q < self.n
                    and not visited[p][q]
                ):
                    if thiefGrid[p][q] < mid:
                        continue

                    queue.append((p, q))
                    visited[p][q] = True
        return False


if __name__ == "__main__":
    testCases = [
        ([[1]], 0),
        ([[0, 1, 1], [0, 0, 0], [0, 0, 0]], 1),
        ([[1, 0, 0], [0, 0, 0], [0, 0, 1]], 0),
        ([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 2),
        ([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 2),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maximumSafenessFactor(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
