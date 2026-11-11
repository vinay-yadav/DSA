"""
Minimum Cost to Acquire Required Items
"""


class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        if cost1 + cost2 <= costBoth:
            return cost1 * need1 + cost2 * need2

        both = min(need1, need2)
        total = costBoth * both

        need1 -= both
        need2 -= both

        if need1 > 0:
            total += need1 * min(cost1, costBoth)
        elif need2 > 0:
            total += need2 * min(cost2, costBoth)

        return total


if __name__ == "__main__":
    testCases = [
        (3, 2, 1, 3, 2, 3),
        (5, 4, 15, 2, 3, 22),
        (5, 4, 15, 0, 0, 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minimumCost(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
