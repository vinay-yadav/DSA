"""
Edit Distance
"""


class Solution:
    def solve(self, A, B):
        n, m = len(A), len(B)
        self.dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        return self.topDown(n - 1, m - 1, A, B)

    def topDown(self, i, j, A, B):
        if i < 0 or j < 0:
            lenA = i + 1
            lenB = j + 1
            return max(lenA, lenB)

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if A[i] == B[j]:
            distance = self.topDown(i - 1, j - 1, A, B)
        else:
            distance = (
                min(
                    self.topDown(i, j - 1, A, B),  # insert
                    self.topDown(i - 1, j, A, B),  # delete
                    self.topDown(i - 1, j - 1, A, B),  # replace
                )
                + 1
            )

        self.dp[i][j] = distance

        return self.dp[i][j]


if __name__ == "__main__":
    testCases = [("abad", "abac", 1), ("Anshuman", "Antihuman", 2)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
