"""
Find Center of Star Graph
"""


class Solution:
    def findCenter1(self, edges: list[list[int]]) -> int:
        n = len(edges) + 1
        degree_count = [0] * (n + 1)

        for u, v in edges:
            degree_count[u] += 1
            degree_count[v] += 1

        node, max_degree = -1, float("-inf")
        for i in range(1, n + 1):
            if degree_count[i] > max_degree:
                max_degree = degree_count[i]
                node = i

        return node

    def findCenter(self, edges):
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]


if __name__ == "__main__":
    testCases = [
        # ([[1, 2], [2, 3], [4, 2]], 2),
        # ([[1, 2], [5, 1], [1, 3], [1, 4]], 1),
        (
            [
                [1, 18],
                [18, 2],
                [3, 18],
                [18, 4],
                [18, 5],
                [6, 18],
                [18, 7],
                [18, 8],
                [18, 9],
                [18, 10],
                [18, 11],
                [12, 18],
                [18, 13],
                [18, 14],
                [15, 18],
                [16, 18],
                [17, 18],
            ],
            18,
        ),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findCenter(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
