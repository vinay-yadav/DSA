"""
Maximum Building Height
"""

from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        m = len(restrictions)

        arr = [[0, 0] for _ in range(m + 2)]

        for i in range(m):
            arr[i] = restrictions[i]

        arr[m] = [1, 0]
        arr[m + 1] = [n, n - 1]

        arr.sort()

        arrLen = len(arr)

        for i in range(arrLen):
            arr[i][1] = min(arr[i][1], arr[i - 1][1] + arr[i][0] - arr[i - 1][0])

        for i in range(arrLen - 2, -1, -1):
            arr[i][1] = min(arr[i][1], arr[i + 1][1] + arr[i + 1][0] - arr[i][0])

        maxBuildingHeight = 0
        for i in range(1, arrLen):
            peak = (
                arr[i - 1][1]
                + (arr[i][0] - arr[i - 1][0] + arr[i][1] - arr[i - 1][1]) // 2
            )
            maxBuildingHeight = max(maxBuildingHeight, peak)
        
        return maxBuildingHeight


if __name__ == "__main__":
    testCases = [
        (10, [[5, 3], [2, 5], [7, 4], [10, 3]], 5),
        (6, [], 5),
        (5, [[2, 1], [4, 1]], 2),
        (
            10,
            [[8, 5], [9, 0], [6, 2], [4, 0], [3, 2], [10, 0], [5, 3], [7, 3], [2, 4]],
            2,
        ),
        (5, [[2, 0]], 3),
        (10, [[5, 1], [3, 0]], 6),
        (10, [[3, 5], [4, 0]], 6),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxBuilding(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
