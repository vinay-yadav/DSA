"""
Cheapest Flights Within K Stops
"""

import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        visited = [[-1 for _ in range(k + 1)] for _ in range(n)]
        adj = defaultdict(list)

        for u, v, dist in flights:
            adj[u].append((dist, v))

        heap = []
        heapq.heappush(heap, (0, src, -1))

        while heap:
            distance, node, hop = heapq.heappop(heap)

            if hop > k:
                continue

            if visited[node][hop] != -1:
                continue

            visited[node][hop] = distance

            for neigh_dist, neigh in adj[node]:
                if hop + 1 <= k and visited[neigh][hop + 1] == -1:
                    heapq.heappush(heap, (distance + neigh_dist, neigh, hop + 1))

        cheapest_price = float("inf")
        for i in range(k + 1):
            if visited[dst][i] == -1:
                continue

            cheapest_price = min(cheapest_price, visited[dst][i])

        return -1 if cheapest_price == float("inf") else cheapest_price  # type: ignore


if __name__ == "__main__":
    testCases = [
        (
            4,
            [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            0,
            3,
            1,
            700,
        ),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
        (
            5,
            [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]],
            2,
            1,
            1,
            -1,
        ),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findCheapestPrice(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
