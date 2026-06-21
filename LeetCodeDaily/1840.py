"""
Maximum Building Height
"""

from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()

        m = len(restrictions)

        """ left pass """
        for i in range(1, m):
            distance = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(
                restrictions[i][1], restrictions[i - 1][1] + distance
            )

        """ right pass """
        for i in range(m - 2, 0, -1):
            distance = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(
                restrictions[i][1], restrictions[i + 1][1] + distance
            )

        """ calculate max """
        maxBuildingHeight = 0
        for i in range(1, m):
            # id1, h1
            prevPos, prevHeight = restrictions[i - 1][0], restrictions[i - 1][1]
            """ id2, h2 """
            currPos, currHeight = restrictions[i][0], restrictions[i][1]

            distance = currPos - prevPos
            heightDiff = abs(prevHeight - currHeight)

            peek = max(prevHeight, currHeight) + (distance - heightDiff) // 2

            maxBuildingHeight = max(maxBuildingHeight, peek)

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
