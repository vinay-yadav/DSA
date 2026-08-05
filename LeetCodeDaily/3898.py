"""
Find the Degree of Each Vertex
"""


class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)

        result = [0] * n
        for i in range(n):
            degree = 0
            for j in range(n):
                if matrix[i][j] == 0:
                    continue

                degree += 1

            result[i] = degree

        return result


if __name__ == "__main__":
    testCases = [
        ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], [2, 2, 2]),
        ([[0, 1, 0], [1, 0, 0], [0, 0, 0]], [1, 1, 0]),
        ([[0]], [0]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findDegrees(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
