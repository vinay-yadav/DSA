"""
Topological Sort
"""

import heapq
from collections import defaultdict


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        indegreeCount = [0] * (A + 1)
        heap = []
        adj = defaultdict(list)

        for u, v in B:
            adj[u].append(v)
            indegreeCount[v] += 1

        for i in range(1, A + 1):
            if indegreeCount[i] == 0:
                heapq.heappush(heap, i)

        processedNodes = []
        while heap:
            currNode = heapq.heappop(heap)
            processedNodes.append(currNode)

            for neigh in adj[currNode]:
                indegreeCount[neigh] -= 1

                if indegreeCount[neigh] == 0:
                    heapq.heappush(heap, neigh)

        return processedNodes


if __name__ == "__main__":
    testCases = [
        (6, [[6, 3], [6, 1], [5, 1], [5, 2], [3, 4], [4, 2]], [5, 6, 1, 3, 4, 2]),
        (3, [[1, 2], [2, 3], [3, 1]], []),
        (
            8,
            [[1, 4], [1, 2], [4, 2], [4, 3], [3, 2], [5, 2], [3, 5], [8, 2], [8, 6]],
            [1, 4, 3, 5, 7, 8, 2, 6],
        ),
        (4, [[1, 4], [2, 3]], [1, 2, 3, 4]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx + 1}: {{{status} -> {result}}}")
