"""
Maximum Ice Cream Bars
"""

from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        iceCreams = 0
        costs.sort()

        for i in range(len(costs)):
            if costs[i] <= coins:
                iceCreams += 1
                coins -= costs[i]
            else:
                break

        return iceCreams


if __name__ == "__main__":
    testCases = [
        ([1, 3, 2, 4, 1], 7, 4),
        ([10, 6, 8, 7, 7, 8], 5, 0),
        ([1, 6, 3, 1, 2, 5], 20, 6),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxIceCream(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
