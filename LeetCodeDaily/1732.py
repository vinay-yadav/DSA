"""
Find the Highest Altitude
"""

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = gain[0]
        maxAltitude = max(0, curr)

        for i in range(1, len(gain)):
            curr += gain[i]
            maxAltitude = max(maxAltitude, curr)

        return maxAltitude


if __name__ == "__main__":
    testCases = [
        ([-5, 1, 5, 0, -7], 1),
        ([-4, -3, -2, -1, 4, 3, 2], 0),
        ([52, -91, 72], 52),
    ]

    for idx, (gains, expected) in enumerate(testCases):
        result = Solution().largestAltitude(gains)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
