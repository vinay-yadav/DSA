"""
Redundant Connection
"""


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        parent = list(range(n))  # parent[i] = i initially
        rank = [0] * n

        for u, v in edges:
            if not self.union(u, v, parent, rank):
                return [u, v]

        return []

    def find_root(self, node, parent):
        if node == parent[node]:
            return node

        parent[node] = self.find_root(parent[node], parent)
        return parent[node]

    def union(self, node_x, node_y, parent, rank) -> bool:
        parent_x = self.find_root(node_x, parent)
        parent_y = self.find_root(node_y, parent)

        if parent_x == parent_y:
            return False

        if rank[parent_x] < rank[parent_y]:
            parent[parent_x] = parent_y
        elif rank[parent_x] > rank[parent_y]:
            parent[parent_y] = parent_x
        else:
            parent[parent_x] = parent_y
            rank[parent_y] += 1

        return True


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
