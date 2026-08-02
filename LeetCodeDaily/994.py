"""
Rotting Oranges
"""

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        q = deque([])

        num_of_ones = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    num_of_ones += 1

                elif grid[i][j] == 2:
                    q.append(((i, j), 0))

        if num_of_ones == 0:
            return 0

        level = 0
        while q:
            (i, j), level = q.popleft()

            for u, v in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + u, j + v

                if not self.isValid(ni, nj, grid, n, m):
                    continue

                grid[ni][nj] = 2
                num_of_ones -= 1

                q.append(((ni, nj), level + 1))

        if num_of_ones != 0:
            return -1

        return level

    def isValid(self, i, j, grid, n, m):
        return i >= 0 and j >= 0 and i < n and j < m and grid[i][j] == 1


if __name__ == "__main__":
    testCases = [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().orangesRotting(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
