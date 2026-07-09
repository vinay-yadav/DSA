"""
Path Existence Queries in a Graph I
"""

from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        componentList = [-1] * n
        result: List[bool] = [False] * len(queries)

        componentList[0] = 0
        componentId = 0

        for i in range(1, n):
            if abs(nums[i] - nums[i - 1]) > maxDiff:
                componentId += 1

            componentList[i] = componentId

        for idx, (u, v) in enumerate(queries):
            result[idx] = componentList[u] == componentList[v]

        return result


if __name__ == "__main__":
    testCases = [
        (2, [1, 3], 1, [[0, 0], [0, 1]], [True, False]),
        (
            4,
            [2, 5, 6, 8],
            2,
            [[0, 1], [0, 2], [1, 3], [2, 3]],
            [False, False, True, True],
        ),
        (2, [52719, 87657], 52, [[0, 0]], [True]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().pathExistenceQueries(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
