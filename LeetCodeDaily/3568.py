"""
Minimum Moves to Clean the Classroom
"""

from collections import deque


class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        maxEnergy = energy

        # flat 1D, sized to actual grid instead of fixed 20x20
        litterBit = [-1] * (m * n)
        litterCount = 0
        startR = startC = -1

        for r in range(m):
            row = classroom[r]
            base = r * n
            for c in range(n):
                ch = row[c]
                if ch == "S":
                    startR, startC = r, c
                elif ch == "L":
                    litterBit[base + c] = litterCount
                    litterCount += 1

        if litterCount == 0:
            return 0

        allCollected = (1 << litterCount) - 1
        maskSize = 1 << litterCount

        # Flat bytearray instead of 4 nested Python lists of bools.
        # index = (r*n+c) * cellStride + e * maskSize + mask
        energyStride = maskSize
        cellStride = (maxEnergy + 1) * maskSize
        totalSize = m * n * (maxEnergy + 1) * maskSize
        seen = bytearray(totalSize)

        def idx(r, c, e, mask):
            return (r * n + c) * cellStride + e * energyStride + mask

        # Precompute cell type once: 0=normal, 1=obstacle, 2=reset
        cellType = bytearray(m * n)
        for r in range(m):
            row = classroom[r]
            base = r * n
            for c in range(n):
                ch = row[c]
                if ch == "X":
                    cellType[base + c] = 1
                elif ch == "R":
                    cellType[base + c] = 2

        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

        startIndex = idx(startR, startC, maxEnergy, 0)
        seen[startIndex] = 1

        q = deque()
        q.append((startR, startC, maxEnergy, 0))
        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == allCollected:
                    return moves

                if e == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    nbase = nr * n + nc
                    ct = cellType[nbase]
                    if ct == 1:
                        continue

                    if ct == 2:
                        nextEnergy = maxEnergy
                        nextMask = mask
                    else:
                        nextEnergy = e - 1
                        bit = litterBit[nbase]
                        nextMask = mask | (1 << bit) if bit != -1 else mask

                    stateIdx = idx(nr, nc, nextEnergy, nextMask)
                    if not seen[stateIdx]:
                        seen[stateIdx] = 1
                        q.append((nr, nc, nextEnergy, nextMask))

            moves += 1

        return -1


if __name__ == "__main__":
    testCases = [
        (["S.", "XL"], 2, 2),
        (["LS", "RL"], 4, 3),
        (["L.S", "RXL"], 3, -1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minMoves(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
