"""
Remove Methods From Project
"""

from collections import defaultdict, deque


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: list[list[int]]
    ) -> list[int]:
        adj = defaultdict(list)
        indegree_count = [0] * n
        suspecious = [False] * n

        for u, v in invocations:
            adj[u].append(v)
            indegree_count[v] += 1

        q = deque([k])
        suspecious[k] = True

        while q:
            curr = q.popleft()

            for neigh in adj[curr]:
                indegree_count[neigh] -= 1

                if not suspecious[neigh]:
                    q.append(neigh)
                    suspecious[neigh] = True

        result = []
        for i in range(n):
            if suspecious[i] and indegree_count[i] > 0:
                return [node for node in range(n)]

            if not suspecious[i]:
                result.append(i)

        return result

    def remainingMethods1(
        self, n: int, k: int, invocations: list[list[int]]
    ) -> list[int]:
        adj = defaultdict(list)
        indegree_count = [0] * n
        visited = [-1] * n

        for u, v in invocations:
            adj[u].append(v)
            indegree_count[v] += 1

        q = deque([k])
        visited[k] = 1

        suspecious_nodes = {k}
        while q:
            curr = q.popleft()

            for neigh in adj[curr]:
                indegree_count[neigh] -= 1

                if visited[neigh] == -1:
                    q.append(neigh)
                    visited[neigh] = 1
                    suspecious_nodes.add(neigh)

        for node in suspecious_nodes:
            if indegree_count[node] != 0:
                return [i for i in range(n)]

        return [i for i in range(n) if i not in suspecious_nodes]


if __name__ == "__main__":
    testCases = [
        (4, 1, [[1, 2], [0, 1], [3, 2]], [0, 1, 2, 3]),
        (5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]], [3, 4]),
        (3, 2, [[1, 2], [0, 1], [2, 0]], []),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().remainingMethods(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
