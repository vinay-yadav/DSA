"""
Find Subtree Sizes After Changes
"""

from collections import defaultdict


class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        adj = defaultdict(list)
        result_size = [1] * n
        last = [-1] * 26

        for idx in range(1, n):
            u = parent[idx]
            v = idx

            adj[u].append(v)

        def dfs(current_node: int) -> None:
            chr = ord(s[current_node]) - ord("a")
            nearest_ancestor = last[chr]
            last[chr] = current_node

            for child in adj[current_node]:
                dfs(child)

            last[chr] = nearest_ancestor

            if current_node != 0:
                new_parent = parent[current_node]

                if nearest_ancestor != -1:
                    new_parent = nearest_ancestor

                parent[current_node] = new_parent
                result_size[new_parent] += result_size[current_node]

        dfs(0)

        return result_size


if __name__ == "__main__":
    testCases = [
        ([-1, 0, 0, 1, 1, 1], "abaabc", [6, 3, 1, 1, 1, 1]),
        ([-1, 0, 4, 0, 1], "abbba", [5, 2, 1, 1, 1]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findSubtreeSizes(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
