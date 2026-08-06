"""
Course Schedule
"""

from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
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

        while q:
            curr = q.popleft()

            for neigh in adj[curr]:
                indegree_count[neigh] -= 1

                if indegree_count[neigh] == 0 and visited[neigh] == -1:
                    visited[neigh] = 1
                    q.append(neigh)

        for i in range(numCourses):
            if indegree_count[i] > 0:
                return False

        return True


if __name__ == "__main__":
    testCases = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().canFinish(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
