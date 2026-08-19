"""
Cinema Seat Allocation
"""

from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        bookedSeats = defaultdict(list)

        for row, seat in reservedSeats:
            bookedSeats[row].append(seat)

        processedVacantBlocks = 0
        for rowData in bookedSeats.values():
            processedVacantBlocks += self.getVacantBlocks(rowData)

        return processedVacantBlocks + (n - len(bookedSeats)) * 2

    def getVacantBlocks(self, rowData) -> int:
        block1 = block2 = block3 = True

        for seat in rowData:
            if seat == 1 or seat == 10:
                continue

            if 2 <= seat <= 5:
                block1 = False

            if 4 <= seat <= 7:
                block2 = False

            if 6 <= seat <= 9:
                block3 = False

        if block1 and block3:
            return 2
        elif block1 or block2 or block3:
            return 1
        return 0


if __name__ == "__main__":
    testCases = [
        (3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]], 4),
        (2, [[2, 1], [1, 8], [2, 6]], 2),
        (4, [[4, 3], [1, 4], [4, 6], [1, 7]], 4),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxNumberOfFamilies(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
