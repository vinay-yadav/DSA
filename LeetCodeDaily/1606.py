"""
Find Servers That Handled Most Number of Requests
"""

from heapq import heappop, heappush


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))
        busy = []
        count = [0] * k

        for i, (start, dur) in enumerate(zip(arrival, load)):
            # Release servers that have finished by this arrival time
            while busy and busy[0][0] <= start:
                _, s = heappop(busy)
                # Re-insert at the next position >= i in the cyclic order,
                # so popping the smallest value gives the first free server at/after i % k
                heappush(free, i + ((s - i) % k))

            if not free:
                continue

            server = heappop(free) % k
            count[server] += 1
            heappush(busy, (start + dur, server))

        best = max(count)
        return [i for i, c in enumerate(count) if c == best]


if __name__ == "__main__":
    testCases = [
        (3, [1, 2, 3, 4, 5], [5, 2, 3, 3, 3], [1]),
        (3, [1, 2, 3, 4], [1, 2, 1, 2], [0]),
        (3, [1, 2, 3], [10, 12, 11], [0, 1, 2]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().busiestServers(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
