"""
Count Islands With Total Value Divisible by K
"""

from collections import deque


class Solution:
    """
    TC: O(n * m)
    SC: O(n * m)
    """

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def countIslands(self, grid: list[list[int]], k: int) -> int:
        """
        BFS
        """
        n, m = len(grid), len(grid[0])

        def bfs(i, j):
            sum_of_islands = grid[i][j]
            grid[i][j] = 0
            q = deque([(i, j)])

            while q:
                i_, j_ = q.popleft()

                for x, y in self.directions:
                    ni, nj = i_ + x, j_ + y

                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] > 0:
                        sum_of_islands += grid[ni][nj]
                        grid[ni][nj] = 0
                        q.append((ni, nj))

            return sum_of_islands

        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and bfs(i, j) % k == 0:
                    islands += 1

        return islands

    def countIslands1(self, grid: list[list[int]], k: int) -> int:
        """
        DFS
        """
        n, m = len(grid), len(grid[0])

        def dfs(i, j) -> int:
            if i < 0 or j < 0 or i == n or j == m or grid[i][j] == 0:
                return 0

            sum_of_islands = grid[i][j]
            grid[i][j] = 0

            for x, y in self.directions:
                ni, nj = i + x, j + y
                sum_of_islands += dfs(ni, nj)

            return sum_of_islands

        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and dfs(i, j) % k == 0:
                    islands += 1

        return islands


if __name__ == "__main__":
    testCases = [
        (
            [
                [0, 2],
                [0, 2],
            ],
            4,
            1,
        ),
        (
            [
                [0, 2, 1, 0, 0],
                [0, 5, 0, 0, 5],
                [0, 0, 1, 0, 0],
                [0, 1, 4, 7, 0],
                [0, 2, 0, 0, 8],
            ],
            5,
            2,
        ),
        (
            [
                [0, 2, 1, 0, 3],
                [0, 5, 0, 0, 5],
                [0, 0, 1, 0, 0],
                [0, 1, 4, 7, 0],
                [0, 2, 0, 0, 8],
            ],
            8,
            3,
        ),
        (
            [
                [3, 0, 3, 0],
                [0, 3, 0, 3],
                [3, 0, 3, 0],
            ],
            3,
            6,
        ),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countIslands(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
