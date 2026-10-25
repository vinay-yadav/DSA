"""
Number of Closed Islands
"""


class Solution:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if self.dfs(i, j, grid, m, n):
                        count += 1

        return count

    def dfs(self, i: int, j: int, grid: list[list[int]], m: int, n: int) -> bool:
        if i < 0 or j < 0 or i == m or j == n:
            return False

        if grid[i][j] == 1:
            return True

        grid[i][j] = 1

        closed = True

        for x, y in self.directions:
            ni, nj = i + x, j + y
            closed = self.dfs(ni, nj, grid, m, n) and closed

        return closed


if __name__ == "__main__":
    testCases = [
        (
            [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0],
            ],
            2,
        ),
        ([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]], 1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().closedIsland(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
