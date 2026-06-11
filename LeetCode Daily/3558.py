"""
Number of Ways to Assign Edge Weights I
"""

from typing import List, Tuple


class Solution:
    MOD = 10**9 + 7

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        nodeAdjMap = dict()

        for u, v in edges:
            if nodeAdjMap.get(u, None) is not None:
                nodeAdjMap[u].append(v)
            else:
                nodeAdjMap[u] = [v]
            
            if nodeAdjMap.get(v, None) is not None:
                nodeAdjMap[v].append(u)
            else:
                nodeAdjMap[v] = [u]

        maxDepth = self.getMaxDepth(nodeAdjMap, 1, -1)

        return int((2 ** (maxDepth - 1)) % self.MOD)

    def getMaxDepth(self, adj, node, parent):
        maxDepth = 0

        for neighbour in adj[node]:
            if neighbour == parent:
                continue

            maxDepth = max(maxDepth, self.getMaxDepth(adj, neighbour, node) + 1)

        return maxDepth


if __name__ == "__main__":
    testCases: List[Tuple[List[List[int]], int]] = [
        ([[1, 2]], 1),
        ([[1, 2], [1, 3], [3, 4], [3, 5]], 2),
    ]

    for idx, (edge, expected) in enumerate(testCases):
        result = Solution().assignEdgeWeights(edge)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
