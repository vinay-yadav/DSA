"""
Course Schedule II
"""

from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegree_count = [0] * numCourses
        visited = [-1] * numCourses
        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[v].append(u)
            indegree_count[u] += 1

        q = deque()

        for i in range(numCourses):
            if indegree_count[i] == 0:
                q.append(i)
                visited[i] = 1

        result = []

        while q:
            curr = q.popleft()
            result.append(curr)

            for neigh in adj[curr]:
                indegree_count[neigh] -= 1

                if indegree_count[neigh] == 0 and visited[neigh] == -1:
                    visited[neigh] = 1
                    q.append(neigh)

        if len(result) != numCourses:
            return []
        return result


if __name__ == "__main__":
    testCases = [
        (2, [[1, 0]], [0, 1]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 2, 1, 3]),
        (1, [], [0]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findOrder(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
