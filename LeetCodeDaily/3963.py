"""
Create Grid With Exactly One Path
"""


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#" for _ in range(n)] for _ in range(m)]

        for i in range(n):
            grid[0][i] = "."

        for i in range(m):
            grid[i][n - 1] = "."

        return ["".join(row) for row in grid]


if __name__ == "__main__":
    testCases = [
        (2, 3, ["..#", "#.."]),
        (3, 3, ["..#", "#..", "##."]),
        (1, 4, ["...."]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().createGrid(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
