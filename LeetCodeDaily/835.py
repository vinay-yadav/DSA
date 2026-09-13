"""
Image Overlap
"""


class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        maxOverlap = 0
        n = len(img1)

        for rowOff in range(-n + 1, n):
            for colOff in range(-n + 1, n):
                count = self.countOverlaps(img1, img2, rowOff, colOff)

                maxOverlap = max(maxOverlap, count)

        return maxOverlap

    def countOverlaps(self, img1, img2, rowOff, colOff) -> int:
        n = len(img1)

        count = 0

        for i in range(n):
            for j in range(n):
                other_i = i + rowOff
                other_j = j + colOff

                if other_i < 0 or other_i >= n or other_j < 0 or other_j >= n:
                    continue

                if img1[i][j] == 1 and img2[other_i][other_j] == 1:
                    count += 1

        return count


if __name__ == "__main__":
    testCases = [
        ([[1]], [[1]], 1),
        ([[0]], [[0]], 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().largestOverlap(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
