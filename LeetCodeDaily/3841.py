"""
Palindromic Path Queries in a Tree
"""

from collections import defaultdict


class Solution:
    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        # ---------- helpers ----------
        def bit(ch: str) -> int:
            return 1 << (ord(ch) - ord("a"))

        chars = [bit(c) for c in s]  # one-hot mask per node, kept current

        # ---------- build tree ----------
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        order = []

        # iterative DFS (recursion would overflow the stack for n = 5 * 10^4)
        stack = [0]
        while stack:
            node = stack.pop()
            tin[node] = len(order)
            order.append(node)
            for nb in adj[node]:
                if nb != parent[node]:
                    parent[nb] = node
                    depth[nb] = depth[node] + 1
                    stack.append(nb)

        size = [1] * n
        for node in reversed(order):
            if parent[node] != -1:
                size[parent[node]] += size[node]
        tout = [tin[i] + size[i] for i in range(n)]  # exclusive end of subtree

        # ---------- binary lifting for LCA ----------
        LOG = max(1, n.bit_length())
        up = [parent[:]] + [[-1] * n for _ in range(LOG - 1)]
        for j in range(1, LOG):
            prev, cur = up[j - 1], up[j]
            for node in range(n):
                if prev[node] != -1:
                    cur[node] = prev[prev[node]]

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff >> j & 1:
                    u = up[j][u]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u, v = up[j][u], up[j][v]
            return parent[u]

        # ---------- Fenwick tree: range-XOR update, point query ----------
        # value at position tin[x] = XOR of chars on the root -> x path
        tree = [0] * (n + 1)

        def _point_xor(i: int, val: int) -> None:
            i += 1
            while i <= n:
                tree[i] ^= val
                i += i & -i

        def xor_subtree(node: int, val: int) -> None:
            _point_xor(tin[node], val)
            if tout[node] < n:
                _point_xor(tout[node], val)

        def path_mask_from_root(node: int) -> int:
            i, res = tin[node] + 1, 0
            while i > 0:
                res ^= tree[i]
                i -= i & -i
            return res

        for node in range(n):
            xor_subtree(node, chars[node])

        # ---------- answer queries ----------
        result = []
        for q in queries:
            kind, a, b = q.split()
            u = int(a)

            if kind == "update":
                new = bit(b)
                xor_subtree(u, chars[u] ^ new)
                chars[u] = new
            else:
                v = int(b)
                l = lca(u, v)
                # root->u and root->v both contain root..lca, which cancels,
                # so XOR lca's own char back in.
                mask = path_mask_from_root(u) ^ path_mask_from_root(v) ^ chars[l]
                # palindrome iff at most one character has odd count
                result.append(mask & (mask - 1) == 0)

        return result


if __name__ == "__main__":
    testCases = [
        (
            3,
            [[0, 1], [1, 2]],
            "aac",
            ["query 0 2", "update 1 b", "query 0 2"],
            [True, False],
        ),
        (
            4,
            [[0, 1], [0, 2], [0, 3]],
            "abca",
            ["query 1 2", "update 0 b", "query 2 3", "update 3 a", "query 1 3"],
            [False, False, True],
        ),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().palindromePath(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
