"""
Last Visited Cell in a Directional Grid
"""


class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        dirs = {
            "L": (0, -1),
            "R": (0, 1),
            "U": (-1, 0),
            "D": (1, 0),
        }

        i = j = 0
        while True:
            visited[i][j] = True

            di, dj = dirs[grid[i][j]]
            ni, nj = i + di, j + dj

            if not (0 <= ni < n and 0 <= nj < m) or visited[ni][nj]:
                return [i, j]

            i, j = ni, nj

    def lastVisitedCell1(self, grid: list[list[str]]) -> list[int]:
        result = [-1] * 2
        n, m = len(grid), len(grid[0])
        visited = [[-1 for _ in range(m)] for _ in range(n)]

        dirs = {
            "L": (0, -1),
            "R": (0, 1),
            "U": (-1, 0),
            "D": (1, 0),
        }

        def dfs(i, j):
            visited[i][j] = 1

            di, dj = dirs[grid[i][j]]
            ni, nj = i + di, j + dj

            if ni < 0 or nj < 0 or ni >= n or nj >= m or visited[ni][nj] != -1:
                result[0], result[1] = i, j
                return

            dfs(ni, nj)

        dfs(0, 0)

        return result


if __name__ == "__main__":
    testCases = [
        ([["R", "D"], ["U", "L"]], [1, 0]),
        ([["R", "R", "R"]], [0, 2]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().lastVisitedCell(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
