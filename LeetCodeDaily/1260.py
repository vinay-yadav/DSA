"""
Shift 2D Grid
"""

import copy


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        TC: O(m * n)
        SC: O(1)
        """
        row, col = len(grid), len(grid[0])
        n = row * col

        k = k % n

        if k == 0:
            return grid

        def reverseList(i, j):
            while i < j:
                r1, c1 = i // col, i % col
                r2, c2 = j // col, j % col

                grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]

                i += 1
                j -= 1

        reverseList(0, n - 1)
        reverseList(0, k - 1)
        reverseList(k, n - 1)

        return grid

    def shiftGrid2(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        TC: O(m * n)
        SC: O(m * n)
        """
        if k == 0:
            return grid

        m, n = len(grid), len(grid[0])

        flatGrid = [grid[i][j] for i in range(m) for j in range(n)]
        flatGridLength = len(flatGrid)

        k = k % flatGridLength

        def reverseList(p, q):
            while p < q:
                flatGrid[p], flatGrid[q] = flatGrid[q], flatGrid[p]
                p += 1
                q -= 1

        reverseList(0, flatGridLength - 1)
        reverseList(0, k - 1)
        reverseList(k, flatGridLength - 1)

        counter = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = flatGrid[counter]
                counter += 1

        return grid

    def shiftGrid1(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        TC: O(m * n)
        SC: O(m * n)
        """
    
        if k == 0:
            return grid

        m, n = len(grid), len(grid[0])

        flatGrid = [grid[i][j] for i in range(m) for j in range(n)]
        flatGridLength = len(flatGrid)

        newGrid = [-1] * flatGridLength

        for i in range(flatGridLength):
            ni = (i + k) % (flatGridLength)
            newGrid[ni] = flatGrid[i]

        counter = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = newGrid[counter]
                counter += 1

        return grid

    def naive(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        TC: O(k *m * n)
        SC: O(m * n)
        """
        if k == 0:
            return grid

        m, n = len(grid), len(grid[0])
        newGrid = [[-1 for _ in range(n)] for _ in range(m)]

        while k > 0:
            for i in range(m):
                for j in range(n):
                    if i == m - 1 and j == n - 1:
                        newGrid[0][0] = grid[i][j]
                    elif j == n - 1:
                        newGrid[i + 1][0] = grid[i][j]
                    else:
                        newGrid[i][j + 1] = grid[i][j]

            k -= 1
            grid = copy.deepcopy(newGrid)

        return newGrid


if __name__ == "__main__":
    testCases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [[9, 1, 2], [3, 4, 5], [6, 7, 8]]),
        (
            [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]],
            4,
            [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]],
        ),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().shiftGrid(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
