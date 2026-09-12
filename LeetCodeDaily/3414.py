"""
Maximum Score if Non-overlapping Interavals
"""


class Node:
    def __init__(self, score=-1, idxs=None):
        self.score = score
        self.idxs = idxs if idxs is not None else []


class Solution:
    K = 4

    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)

        # TC: O(n)
        for idx, interval in enumerate(intervals):
            interval.append(idx)

        # TC: O(nlogn)
        intervals.sort()

        nextIdx = [0] * n

        # TC: O(nlogn)
        for idx in range(n):
            end = intervals[idx][1]
            nextIdx[idx] = self.findNext(intervals, end, n)  # TC: O(logn)

        dp = [[Node() for _ in range(self.K + 1)] for _ in range(n + 1)]

        # TC: O(n)
        def solve(i, k) -> Node:
            if k == 0 or i >= n:
                return Node()

            if dp[i][k].score != -1:
                return dp[i][k]

            _, _, weight, idx = intervals[i]
            j = nextIdx[i]

            # skip interval i
            skip = solve(i + 1, k)

            # take interval i
            temp = solve(j, k - 1)
            take = Node(score=temp.score + weight, idxs=sorted(temp.idxs + [idx]))

            if skip.score > take.score:
                result = skip
            elif skip.score < take.score:
                result = take
            else:
                result = skip if skip.idxs < take.idxs else take

            dp[i][k] = result

            return dp[i][k]

        return solve(0, self.K).idxs

    def findNext(self, intervals, end, n):
        low, high = 0, n - 1

        result = n

        while low <= high:
            mid = low + (high - low) // 2

            if intervals[mid][0] > end:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result


if __name__ == "__main__":
    testCases = [
        ([[1, 3, 2], [4, 5, 2], [1, 5, 5], [6, 9, 3], [6, 7, 1], [8, 9, 1]], [2, 3]),
        (
            [
                [5, 8, 1],
                [6, 7, 7],
                [4, 7, 3],
                [9, 10, 6],
                [7, 8, 2],
                [11, 14, 3],
                [3, 5, 5],
            ],
            [1, 3, 5, 6],
        ),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maximumWeight(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
