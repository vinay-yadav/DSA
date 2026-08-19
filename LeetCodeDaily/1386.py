"""
Cinema Seat Allocation
"""

from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        """
        T.C: O(reservedSeats)
        S.C: O(reservedSeats)
        """
        bookedSeats = defaultdict(int)

        for row, seat in reservedSeats:
            bookedSeats[row] |= 1 << seat

        group1 = 1 << 2 | 1 << 3 | 1 << 4 | 1 << 5
        group2 = 1 << 4 | 1 << 5 | 1 << 6 | 1 << 7
        group3 = 1 << 6 | 1 << 7 | 1 << 8 | 1 << 9

        result = 0
        for value in bookedSeats.values():
            isGroup1Available = value & group1 == 0
            isGroup2Available = value & group2 == 0
            isGroup3Available = value & group3 == 0

            if isGroup1Available and isGroup3Available:
                result += 2
            elif isGroup1Available or isGroup2Available or isGroup3Available:
                result += 1

        return result + (n - len(bookedSeats)) * 2

    def maxNumberOfFamilies1(self, n: int, reservedSeats: list[list[int]]) -> int:
        """
        T.C: O(reservedSeats)
        S.C: O(reservedSeats)
        """
        bookedSeats = defaultdict(list)

        for row, seat in reservedSeats:
            bookedSeats[row].append(seat)

        processedVacantBlocks = 0
        for rowData in bookedSeats.values():
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
                processedVacantBlocks += 2
            elif block1 or block2 or block3:
                processedVacantBlocks += 1

        return processedVacantBlocks + (n - len(bookedSeats)) * 2


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
