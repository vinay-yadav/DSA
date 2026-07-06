"""
Remove Covered Intervals
"""

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        TC: O(nlogn)
        SC: O(1)
        """

        intervals.sort(key=lambda x: (x[0], -x[1]))

        result = 1
        lastCheck = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][1] <= lastCheck[1]:
                continue

            lastCheck = intervals[i]
            result += 1

        return result

    def removeCoveredIntervals2(self, intervals: List[List[int]]) -> int:
        """
        TC: O(nlogn)
        SC: O(n)
        """

        intervals.sort(key=lambda x: (x[0], -x[1]))

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][1] <= result[-1][1]:
                continue

            result.append(intervals[i])

        return len(result)

    def removeCoveredIntervals1(self, intervals: List[List[int]]) -> int:
        """
        TC: O(nlogn)
        SC: O(n)
        """

        intervals.sort(key=lambda x: (x[0], -x[1]))

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            a, b = result[-1]
            c, d = intervals[i]

            if a <= c and d <= b:
                continue

            result.append(intervals[i])

        return len(result)


if __name__ == "__main__":
    testCases = [
        ([[1, 4], [3, 6], [2, 8]], 2),
        ([[1, 4], [2, 3]], 1),
        ([[6, 8], [2, 4], [1, 5], [5, 9]], 2),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().removeCoveredIntervals(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
