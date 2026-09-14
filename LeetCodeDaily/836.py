"""
Rectangle Overlap
"""


class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1, y1, x2, y2 = rec1
        p1, q1, p2, q2 = rec2

        return max(x1, p1) < min(x2, p2) and max(y1, q1) < min(y2, q2)


if __name__ == "__main__":
    testCases = [
        ([0, 0, 2, 2], [1, 1, 3, 3], True),
        ([0, 0, 1, 1], [1, 0, 2, 1], False),
        ([0, 0, 1, 1], [2, 2, 3, 3], False),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().isRectangleOverlap(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
