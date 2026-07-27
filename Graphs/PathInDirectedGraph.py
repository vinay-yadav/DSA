"""
Path in Directed Graph
"""

from collections import deque


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adj = [[] for _ in range(A + 1)]
        visited = [0] * (A + 1)

        for u, v in B:
            adj[u].append(v)

        return 1 if self.bfs(1, visited, adj, A) else 0

    def bfs(self, node, visited, adj, target):
        q = deque([node])
        visited[node] = 1

        while q:
            ele = q.popleft()

            for neigh in adj[ele]:
                if neigh == target:
                    return True

                if not visited[neigh]:
                    visited[neigh] = 1
                    q.append(neigh)

        return False

    def dfs(self, node, visited, adj, target):
        visited[node] = 1

        if node == target:
            return True

        for neigh in adj[node]:
            if not visited[neigh]:
                if self.dfs(neigh, visited, adj, target):
                    return True

        return False


if __name__ == "__main__":
    testCases = [
        (5, [[1, 2], [4, 1], [2, 4], [3, 4], [5, 2], [1, 3]], 0),
        (5, [[1, 2], [2, 3], [3, 4], [4, 5]], 1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
