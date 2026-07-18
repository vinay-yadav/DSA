"""
Regular Expression Match
"""


class Solution:
    def solve(self, A, B):
        n, m = len(A), len(B)
        self.dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        return self.topDown(n - 1, m - 1, A, B)

    def topDown(self, i, j, A, B):
        if i < 0 and j < 0:
            return 1
        elif i >= 0 and j < 0:
            return 0
        elif i < 0 and j >= 0:
            for k in range(j + 1):
                if 97 <= ord(B[k]) <= 122 or B[k] == "?":
                    return 0
            return 1

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if A[i] == B[j]:
            match = self.topDown(i - 1, j - 1, A, B)
        else:
            if B[j] == "?":
                match = self.topDown(i - 1, j - 1, A, B)
            elif B[j] == "*":
                match = self.topDown(i - 1, j, A, B) | self.topDown(i, j - 1, A, B)
            else:
                match = 0

        self.dp[i][j] = match

        return self.dp[i][j]


if __name__ == "__main__":
    testCases = [("aaa", "a*", 1), ("acz", "a?a", 0), ("cc", "?", 0)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
