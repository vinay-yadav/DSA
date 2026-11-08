"""
Count Servers that Communicate
"""


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        """
        TC: O(m * n)
        SC: O(m + n)
        """
        m, n = len(grid), len(grid[0])

        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if rows[i] > 1 or cols[j] > 1:
                        result += 1

        return result

    def countServers1(self, grid: list[list[int]]) -> int:
        """
        TC: O(m * n * (m + n))
        SC: O(1)
        """
        m, n = len(grid), len(grid[0])

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                can_communicate = False

                for x in range(m):
                    if grid[x][j] == 1 and x != i:
                        can_communicate = True
                        result += 1
                        break

                if can_communicate:
                    continue

                for x in range(n):
                    if grid[i][x] == 1 and x != j:
                        result += 1
                        break

        return result


if __name__ == "__main__":
    testCases = [
        ([[1, 0], [0, 1]], 0),
        ([[1, 0], [1, 1]], 3),
        ([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countServers(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
