import heapq
from collections import defaultdict


def prims(n, nodes):
    adj = defaultdict(list)

    for u, v, d in nodes:
        adj[u].append((d, v))
        adj[v].append((d, u))

    visited = [-1] * (n + 1)

    heap = adj[1][:]
    heapq.heapify(heap)
    visited[1] = 1

    result = 0

    while heap:
        distance, node = heapq.heappop(heap)

        if visited[node] == 1:
            continue

        visited[node] = 1
        result += distance

        for v in adj[node]:
            heapq.heappush(heap, v)

    return result


if __name__ == "__main__":
    print(
        prims(
            6,
            [
                [1, 2, 4],
                [1, 4, 5],
                [2, 4, 3],
                [2, 3, 6],
                [4, 3, 3],
                [4, 5, 10],
                [3, 6, 5],
                [3, 5, 4],
                [5, 6, 2],
            ],
        )
    )
