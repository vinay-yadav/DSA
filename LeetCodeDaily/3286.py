"""
Find a Safe Walk Through a Grid
"""

from collections import deque
from typing import List, Tuple


class Solution:
    def __init__(self) -> None:
        self.directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])
        result = [[float("inf")] * m for _ in range(n)]
        result[0][0] = grid[0][0]

        queue = deque([(0, 0)])
        while queue:
            i, j = queue.popleft()

            for dir in self.directions:
                new_i = i + dir[0]
                new_j = j + dir[1]

                if new_i >= n or new_i < 0 or new_j >= m or new_j < 0:
                    continue

                if result[new_i][new_j] > result[i][j] + grid[new_i][new_j]:
                    result[new_i][new_j] = result[i][j] + grid[new_i][new_j]

                    if grid[new_i][new_j] == 0:
                        queue.appendleft((new_i, new_j))
                    else:
                        queue.append((new_i, new_j))

        x = result[n - 1][m - 1]
        if health - x >= 1:
            return True
        return False


if __name__ == "__main__":
    testCases: List[Tuple[List[List[int]], int, bool]] = [
        ([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1, True),
        (
            [
                [0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0],
            ],
            3,
            False,
        ),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 5, True),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findSafeWalk(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
