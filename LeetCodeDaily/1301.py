"""
Number of Paths with Max Score
"""

from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        self.MOD = 1000000007
        self.n = len(board)
        self.t = [[(-1, -1) for _ in range(self.n)] for _ in range(self.n)]

        score, path = self.solve(self.n - 1, self.n - 1, board)
        return [score, path]

    def solve(self, i, j, board) -> List[int]:
        if board[i][j] == "E":
            return [0, 1]

        if board[i][j] == "X":
            return [0, 0]

        if self.t[i][j] != (-1, -1):
            return self.t[i][j]

        ch = board[i][j]

        # Up
        upScore, upPath = self.directionalMove(i - 1, j, board, ch)

        # left
        leftScore, leftPath = self.directionalMove(i, j - 1, board, ch)

        # diagonal
        diagScore, diagPath = self.directionalMove(i - 1, j - 1, board, ch)

        if upScore == leftScore == diagScore:
            bestScore = upScore
            bestPath = upPath + leftPath + diagPath

        elif upScore == leftScore:
            bestScore = upScore
            bestPath = upPath + leftPath

            if diagScore > bestScore or (
                diagScore == bestScore and diagPath > bestPath
            ):
                bestScore = diagScore
                bestPath = diagPath

        elif leftScore == diagScore:
            bestScore = leftScore
            bestPath = leftPath + diagPath

            if upScore > bestScore or (upScore == bestScore and upPath > bestPath):
                bestScore = upScore
                bestPath = upPath

        else:
            bestScore = upScore
            bestPath = upPath

            if leftScore > bestScore or (
                leftScore == bestScore and leftPath > bestPath
            ):
                bestPath = leftPath
                bestScore = leftScore

            if diagScore > bestScore or (
                diagScore == bestScore and diagPath > bestPath
            ):
                bestPath = diagPath
                bestScore = diagScore

        self.t[i][j] = (bestScore, bestPath % self.MOD)
        return [bestScore, bestPath % self.MOD]

    def directionalMove(self, i, j, board, ch):
        score = path = 0
        if self.isValid(i, j, board):
            score, path = self.solve(i, j, board)

            if path > 0:
                score += self.getIntScore(ch)
        return score, path

    def isValid(self, i, j, board):
        return i >= 0 and i < self.n and j >= 0 and j < self.n and board[i][j] != "X"

    def getIntScore(self, ch) -> int:
        if ch.isnumeric():
            return int(ch)
        return 0


if __name__ == "__main__":
    testCases = [
        (["E23", "2X2", "12S"], [7, 1]),
        (["E12", "1X1", "21S"], [4, 2]),
        (["E11", "XXX", "11S"], [0, 0]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().pathsWithMaxScore(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
