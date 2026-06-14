"""
Number of Ways to Assign Edge Weights II
"""

from collections import deque
from typing import List


class Solution:
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        MOD = 10**9 + 7

        n = len(edges) + 1  # n-1 edges => n nodes

        # Build adjacency list (1-indexed)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Binary lifting setup
        LOG = max(1, n.bit_length())
        depth = [0] * (n + 1)
        parent = [[-1] * (n + 1) for _ in range(LOG)]

        # BFS from root=1 to fill depth and parent[0]
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True

        while queue:
            node = queue.popleft()
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    depth[nei] = depth[node] + 1
                    parent[0][nei] = node
                    queue.append(nei)

        # Build binary lifting table
        for k in range(1, LOG):
            for v in range(1, n + 1):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]

        def lca(u, v):
            # Make u the deeper node
            if depth[u] < depth[v]:
                u, v = v, u
            # Bring u up to same depth as v
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = parent[k][u]
            if u == v:
                return u
            # Lift both until LCA found
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        results = []
        for u, v in queries:
            l = lca(u, v)
            k = depth[u] + depth[v] - 2 * depth[l]  # edge count on path
            results.append(0 if k == 0 else pow(2, k - 1, MOD))

        return results


if __name__ == "__main__":
    testCases = [
        ([[1, 2], [1, 3], [3, 4], [3, 5]], [[1, 4], [3, 4], [2, 5]], [2, 1, 4]),
        ([[1, 2]], [[1, 1], [1, 2]], [0, 1]),
    ]

    for idx, (edges, queries, expected) in enumerate(testCases):
        result = Solution().assignEdgeWeights(edges, queries)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
