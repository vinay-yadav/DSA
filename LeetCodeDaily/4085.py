"""
Find Root of a Colored Tree
"""

from collections import defaultdict


class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        next_color = {"R": "B", "B": "W", "W": "R"}
        n = len(colors)

        degree = [0] * n
        has_parent = [False] * n

        for u, v in edges:
            degree[u] += 1
            degree[v] += 1

            if colors[u] == next_color[colors[v]]:
                # v is u's parent
                has_parent[u] = True
            elif colors[v] == next_color[colors[u]]:
                # u is v's parent
                has_parent[v] = True

        roots = [node for node in range(n) if not has_parent[node]]

        if len(roots) != 1:
            return -1

        root = roots[0]

        # root has no parent edge, so all its edges are children
        return root if degree[root] <= 2 else -1

    def findColoredRoot1(self, edges: list[list[int]], colors: str) -> int:
        next_colour = {"R": "B", "B": "W", "W": "R"}
        children = set()

        adj = defaultdict(list)
        for u, v in edges:
            if colors[u] == next_colour[colors[v]]:
                children.add(u)
            elif colors[v] == next_colour[colors[u]]:
                children.add(v)

            adj[u].append(v)
            adj[v].append(u)

        root_candidates = set()
        for node in range(len(colors)):
            if node not in children:
                root_candidates.add(node)

        if len(root_candidates) != 1:
            return -1

        root = next(iter(root_candidates))

        # root can have at most 2 children
        return root if len(adj[root]) < 3 else -1


if __name__ == "__main__":
    testCases = [
        ([[3, 1], [3, 2], [1, 4], [2, 0]], "BRRWB", 3),
        ([[0, 1], [1, 2], [2, 3]], "RBRB", -1),
        ([[0, 1], [0, 2], [0, 3]], "RBBB", -1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findColoredRoot(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
