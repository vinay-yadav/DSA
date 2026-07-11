"""
Count the Number of Complete Components
"""

from collections import defaultdict, deque
from typing import List


class DSU:
    def __init__(self, n) -> None:
        self.parent = [-1] * n
        self.size = [1] * n

        for i in range(n):
            self.parent[i] = i

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_par = self.find(x)
        y_par = self.find(y)

        if x_par == y_par:
            return

        if self.size[x_par] > self.size[y_par]:
            self.parent[y_par] = x_par
            self.size[x_par] += self.size[y_par]

        else:
            self.parent[x_par] = y_par
            self.size[y_par] += self.size[x_par]


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        mp = defaultdict(int)

        for u, v in edges:
            dsu.union(u, v)

        for u, v in edges:
            root = dsu.find(u)
            mp[root] += 1

        result = 0

        for i in range(n):
            if dsu.find(i) == i:
                v = dsu.size[i]
                e = mp[i]

                if (v * (v - 1)) // 2 == e:
                    result += 1

        return result

    def countCompleteComponents2(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        result = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue

            v, e = self.bfs(i, adj, visited)

            if (v * (v - 1)) == e:
                result += 1

        return result

    def bfs(self, node, adj, visited):
        queue = deque([node])
        visited[node] = True
        v = e = 0

        while queue:
            curr = queue.popleft()
            visited[curr] = True

            v += 1
            e += len(adj[curr])

            for ngbr in adj[curr]:
                if not visited[ngbr]:
                    visited[ngbr] = True
                    queue.append(ngbr)

        return v, e

    def dfs(self, node, adj, visited):
        visited[node] = True
        v = 1
        e = len(adj[node])

        for ngbr in adj[node]:
            if not visited[ngbr]:
                nv, ne = self.dfs(ngbr, adj, visited)

                v += nv
                e += ne

        return v, e


if __name__ == "__main__":
    testCases = [
        (6, [[0, 1], [0, 2], [1, 2], [3, 4]], 3),
        (6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]], 1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countCompleteComponents(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
