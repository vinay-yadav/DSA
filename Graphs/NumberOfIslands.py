"""
Number of Islands
"""


class Solution:
    def __init__(self) -> None:
        self.directions = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
        ]

    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A):
        n, m = len(A), len(A[0])

        ans = 0
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    ans += 1
                    self.dfs(i, j, A, n, m)
        return ans

    def dfs(self, i, j, grid, n, m):
        grid[i][j] = 2

        for u, v in self.directions:
            ni, nj = i + u, j + v

            if self.isValid(ni, nj, grid, n, m):
                self.dfs(ni, nj, grid, n, m)

    def isValid(self, i, j, grid, n, m):
        return i >= 0 and j >= 0 and i < n and j < m and grid[i][j] == 1


if __name__ == "__main__":
    testCases = [
        (
            [
                [0, 1, 0],
                [0, 0, 1],
                [1, 0, 0],
            ],
            2,
        ),
        (
            [
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 0, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1],
            ],
            5,
        ),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
