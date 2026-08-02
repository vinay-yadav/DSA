"""
Check Bipartite Graph
"""

from collections import defaultdict


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        colour = [-1] * A

        adj = defaultdict(list)
        for u, v in B:
            adj[u].append(v)
            adj[v].append(u)

        def isBipartite(node, chromaticColour) -> int:
            colour[node] = chromaticColour

            for neigh in adj[node]:
                if colour[neigh] == colour[node]:
                    return 0

                if colour[neigh] == -1:
                    if not isBipartite(neigh, chromaticColour ^ 1):
                        return 0
            return 1

        for i in range(A):
            if colour[i] != -1:
                continue

            if not isBipartite(i, 0):
                return 0

        return 1


if __name__ == "__main__":
    testCases = [
        (2, [[0, 1]], 1),
        (3, [[0, 1], [0, 2], [1, 2]], 0),
        (6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]], 1),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]], 0),
        (
            69,
            [
                [40, 64],
                [29, 60],
                [26, 43],
                [29, 32],
                [32, 47],
                [42, 61],
                [48, 61],
                [26, 52],
                [24, 34],
                [35, 55],
                [14, 60],
                [53, 62],
                [61, 63],
                [13, 53],
                [16, 62],
                [62, 64],
                [56, 68],
                [2, 23],
                [7, 55],
                [3, 60],
                [32, 51],
                [2, 18],
                [1, 43],
                [5, 37],
                [4, 51],
                [27, 55],
                [15, 30],
                [13, 65],
                [7, 13],
                [28, 48],
                [36, 50],
                [3, 7],
                [30, 46],
                [1, 35],
                [47, 68],
                [37, 62],
                [37, 58],
                [8, 22],
                [19, 45],
                [6, 64],
                [9, 55],
                [32, 46],
                [48, 56],
                [26, 59],
                [8, 46],
                [44, 66],
                [50, 60],
                [40, 46],
                [30, 68],
                [26, 44],
                [5, 32],
                [9, 34],
                [36, 45],
                [47, 48],
            ],
            0,
        ),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx + 1}: {{{status} -> {result}}}")
