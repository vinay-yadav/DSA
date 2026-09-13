"""
Cyclically Shift Rows and Columns©leetcode
"""


class Solution:
    def cyclicShift(
        self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]
    ) -> list[list[int]]:
        num_rows, num_cols = len(grid), len(grid[0])

        def reverse_row(row_idx, lo, hi):
            """Reverse grid[row_idx][lo..hi] in place."""
            while lo < hi:
                grid[row_idx][lo], grid[row_idx][hi] = (
                    grid[row_idx][hi],
                    grid[row_idx][lo],
                )
                lo += 1
                hi -= 1

        def reverse_col(col_idx, lo, hi):
            """Reverse grid[lo..hi][col_idx] in place."""
            while lo < hi:
                grid[lo][col_idx], grid[hi][col_idx] = (
                    grid[hi][col_idx],
                    grid[lo][col_idx],
                )
                lo += 1
                hi -= 1

        # Left-shift each row i by rowShift[i]
        for i in range(num_rows):
            k = rowShift[i] % num_cols
            if k == 0:
                continue
            reverse_row(i, 0, k - 1)
            reverse_row(i, k, num_cols - 1)
            reverse_row(i, 0, num_cols - 1)

        # Upward-shift each column j by colShift[j]
        for j in range(num_cols):
            k = colShift[j] % num_rows
            if k == 0:
                continue
            reverse_col(j, 0, k - 1)
            reverse_col(j, k, num_rows - 1)
            reverse_col(j, 0, num_rows - 1)

        return grid


if __name__ == "__main__":
    testCases = [
        (2, [[1, 2], [3, 4]], [1, 0], [0, 1], [[2, 4], [3, 1]]),
        (
            3,
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 0],
            [2, 2, 1],
            [[7, 8, 5], [2, 3, 9], [6, 4, 1]],
        ),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().cyclicShift(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
