"""
Minimum Score of a Path Between Two Cities
"""

from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, dist in roads:
            adj[u].append((v, dist))
            adj[v].append((u, dist))

        visited = [False] * (n + 1)
        answer = float("inf")

        def deapthFirstSearch(node):
            nonlocal answer
            visited[node] = True

            for neighbor, dist in adj[node]:
                answer = min(answer, dist)

                if not visited[neighbor]:
                    deapthFirstSearch(neighbor)

        deapthFirstSearch(1)

        return answer


if __name__ == "__main__":
    testCases = [
        (4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5),
        (4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2),
        (
            20,
            [
                [18, 20, 9207],
                [14, 12, 1024],
                [11, 9, 3056],
                [8, 19, 416],
                [3, 18, 5898],
                [17, 3, 6779],
                [13, 15, 3539],
                [15, 11, 1451],
                [19, 2, 3805],
                [9, 8, 2238],
                [1, 16, 618],
                [16, 14, 55],
                [17, 7, 6903],
                [12, 13, 1559],
                [2, 17, 3693],
            ],
            55,
        ),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minScore(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
