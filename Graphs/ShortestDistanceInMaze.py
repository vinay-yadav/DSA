"""
Shortest Distance in a Maze
"""

from collections import deque


class Solution:
    def __init__(self) -> None:
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        n, m = len(A), len(A[0])
        si, sj = B
        ti, tj = C

        visited = [[0 for _ in range(m)] for _ in range(n)]

        return self.bfs(si, sj, A, n, m, ti, tj, visited)

    def bfs(self, si, sj, grid, n, m, ti, tj, visited) -> int:
        q = deque([((si, sj), 0)])
        visited[si][sj] = 1

        while q:
            coord, level = q.popleft()

            for u, v in self.directions:
                ni, nj = coord[0] + u, coord[1] + v

                if not self.isValid(ni, nj, grid, visited, n, m):
                    continue

                if ni == ti and nj == tj:
                    return level + 1

                visited[ni][nj] = 1
                q.append(((ni, nj), level + 1))

        return -1

    def isValid(self, i, j, grid, visited, n, m):
        return (
            i >= 0
            and j >= 0
            and i < n
            and j < m
            and grid[i][j] != 1
            and visited[i][j] != 1
        )


if __name__ == "__main__":
    testCases = [
        ([[0, 0], [0, 0]], [0, 0], [0, 1], 1),
        ([[0, 1], [1, 0]], [0, 0], [1, 1], -1),
        ([[0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]], [0, 0], [3, 3], -1),
        ([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]], [0, 0], [3, 3], 6),
        ([[0, 0, 0], [1, 1, 0], [0, 0, 0]], [0, 0], [2, 0], 6),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
