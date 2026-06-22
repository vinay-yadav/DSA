"""
Maximum Ice Cream Bars
"""

from typing import List, Tuple


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        countList = [0] * (max(costs) + 1)

        for i in range(len(costs)):
            cost = costs[i]
            countList[cost] += 1

        maxIce = 0
        for cost in range(1, len(countList)):
            if countList[cost] == 0:
                continue

            if cost > coins:
                break

            quantity = min(countList[cost], coins // cost)
            coins -= cost * quantity
            maxIce += quantity

        return maxIce


if __name__ == "__main__":
    testCases: List[Tuple[List[int], int, int]] = [
        ([1, 3, 2, 4, 1], 7, 4),
        ([10, 6, 8, 7, 7, 8], 5, 0),
        ([1, 6, 3, 1, 2, 5], 20, 6),
        ([4, 7, 6, 4, 4, 2, 2, 4, 8, 8], 41, 9),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxIceCream(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
