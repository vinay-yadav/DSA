"""
Process Tasks Using Servers
"""

import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers, busy_servers = [], []

        for idx, weight in enumerate(servers):
            heapq.heappush(free_servers, (weight, idx))

        ans = []
        for current_time, task in enumerate(tasks):
            while busy_servers and current_time >= busy_servers[0][0]:
                _, weight, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, idx))

            if free_servers:
                weight, idx = heapq.heappop(free_servers)
                finish_time = current_time + task
            else:
                busy_until, weight, idx = heapq.heappop(busy_servers)
                finish_time = busy_until + task

            ans.append(idx)
            heapq.heappush(busy_servers, (finish_time, weight, idx))

        return ans


if __name__ == "__main__":
    testCases = [
        ([3, 3, 2], [1, 2, 3, 2, 1, 2], [2, 2, 0, 2, 1, 2]),
        ([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1], [1, 4, 1, 4, 1, 3, 2]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().assignTasks(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
