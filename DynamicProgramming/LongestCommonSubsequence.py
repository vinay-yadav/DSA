"""
Longest Common Subsequence
"""


class Solution:
    def solve(self, A, B):
        n, m = len(A), len(B)
        self.dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        return self.topDown(n - 1, m - 1, A, B)

    def topDown(self, i, j, A, B):
        if i < 0 or j < 0:
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if A[i] == B[j]:
            lcs = self.topDown(i - 1, j - 1, A, B) + 1
        else:
            lcs = max(self.topDown(i - 1, j, A, B), self.topDown(i, j - 1, A, B))

        self.dp[i][j] = lcs

        return self.dp[i][j]


if __name__ == "__main__":
    testCases = [("abbcdgf", "bbadcgf", 5), ("aaaaaa", "ababab", 3)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
