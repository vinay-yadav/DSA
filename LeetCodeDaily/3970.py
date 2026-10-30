"""
Shortest Path With At Most K Consecutive Identical Characters
"""

import heapq
from collections import defaultdict


class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        INF = float("inf")
        dist = [[INF] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        heap = [(0, 0, 1)]

        while heap:
            d, node, run = heapq.heappop(heap)

            if d > dist[node][run]:
                continue

            if node == n - 1:
                return d

            for neigh, w in adj[node]:
                new_run = run + 1 if labels[neigh] == labels[node] else 1
                if new_run > k:
                    continue

                nd = d + w
                if nd < dist[neigh][new_run]:
                    dist[neigh][new_run] = nd
                    heapq.heappush(heap, (nd, neigh, new_run))

        return -1


if __name__ == "__main__":
    testCases = [
        (3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 1, 3),
        (3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 2, 2),
        (3, [[0, 1, 1], [1, 2, 1]], "aaa", 2, -1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().shortestPath(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
