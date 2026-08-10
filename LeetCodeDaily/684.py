"""
Redundant Connection
"""


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        parent = list(range(n))  # parent[i] = i initially

        for u, v in edges:
            pu = self.find_root(u, parent)
            pv = self.find_root(v, parent)

            if pu == pv:
                return [u, v]

            # union by smaller root value — only touch the roots
            if pu < pv:
                parent[pv] = pu
            else:
                parent[pu] = pv

        return []

    def find_root(self, node, parent):
        if node == parent[node]:
            return node

        parent[node] = self.find_root(parent[node], parent)
        return parent[node]


if __name__ == "__main__":
    testCases = [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
        ([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]], [2, 5]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findRedundantConnection(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
