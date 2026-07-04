"""
Network Recovery Pathways
"""

import heapq
from typing import List


class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n = len(online)
        left, right = float("inf"), float("-inf")

        adj = dict()
        for edge in edges:
            u, v, cost = edge[0], edge[1], edge[2]

            if not online[u] or not online[v]:
                continue

            if adj.get(u):
                adj[u].append((v, cost))
            else:
                adj[u] = [(v, cost)]

            left = min(left, cost)
            right = max(right, cost)

        answer = -1
        while left <= right:
            mid: int = left + (right - left) // 2

            if self.check(mid, n, k, adj):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer

    def check(self, mid, n, k, adj):
        result = [float("inf")] * n
        result[0] = 0

        heap = []
        heapq.heappush(heap, (0, 0))

        while heap:
            d, node = heapq.heappop(heap)

            if d > k:
                return False

            if node == n - 1:
                return True

            if result[node] < d:
                continue

            for vec in adj.get(node, []):
                ngbr = vec[0]
                cost = vec[1]

                if cost < mid:
                    continue

                if d + cost < result[ngbr]:
                    result[ngbr] = d + cost
                    heapq.heappush(heap, (d + cost, ngbr))

        return False


if __name__ == "__main__":
    testCases = [
        (
            [[0, 1, 5], [1, 3, 10], [0, 2, 3], [2, 3, 4]],
            [True, True, True, True],
            10,
            3,
        ),
        (
            [[0, 1, 7], [1, 4, 5], [0, 2, 6], [2, 3, 6], [3, 4, 2], [2, 4, 6]],
            [True, True, True, False, True],
            12,
            6,
        ),
        ([[1, 2, 64]], [True, True, True], 172, -1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findMaxPathScore(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
