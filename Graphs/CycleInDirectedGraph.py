"""
Cycle in Directed Graph
"""


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adj = [[] for _ in range(A + 1)]
        visited = [0] * (A + 1)

        for u, v in B:
            adj[u].append(v)

        for node in range(1, A + 1):
            if visited[node] == 2:
                continue

            if self.iterative_dfs(node, visited, adj):
                return 1

        return 0

    def iterative_dfs(self, start_node, visited, adj):
        stack = [(start_node, False)]

        while stack:
            curr = stack.pop()
            node, is_leaving = curr

            if is_leaving:
                visited[node] = 2
                continue

            if visited[node] != 0:
                continue

            visited[node] = 1
            stack.append((node, True))

            for neigh in adj[node]:
                if visited[neigh] == 1:
                    return True

                elif visited[neigh] == 0:
                    stack.append((neigh, False))

        return False

    def dfs(self, node, visited, adj):
        visited[node] = 1

        for neigh in adj[node]:
            if visited[neigh] == 1:
                return True
            elif visited[neigh] == 0:
                if self.dfs(neigh, visited, adj):
                    return True

        visited[node] = 2
        return False


if __name__ == "__main__":
    testCases = [
        (
            5,
            [[1, 2], [4, 1], [2, 4], [3, 4], [5, 2], [1, 3]],
            1,
        ),
        (
            5,
            [[1, 2], [2, 3], [3, 4], [4, 5]],
            0,
        ),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
