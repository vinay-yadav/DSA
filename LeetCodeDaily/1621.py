"""
Number of Sets of K Non-Overlapping Line Segments
"""


class Solution:
    MOD = 1_000_000_007

    def numberOfSets(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

        # Base case: 0 segments
        for i in range(n + 1):
            dp[0][i] = 1

        for segments in range(1, k + 1):
            # suffix sum of previous row
            prev_row_sum = [0] * (n + 1)

            for x in range(n - 1, -1, -1):
                prev_row_sum[x] = (prev_row_sum[x + 1] + dp[segments - 1][x]) % self.MOD

            for i in range(n - 1, -1, -1):
                skip = dp[segments][i + 1]
                take = prev_row_sum[i + 1]

                dp[segments][i] = (skip + take) % self.MOD

        return dp[k][0]

    def naiveTopDown(self, n: int, k: int) -> int:
        """
        TC: O(n^2.k)
        SC: O(n.k)
        """
        dp = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

        def recursive(i, segment_length):
            if i >= n:
                return 0

            if segment_length == k:
                return 1

            if dp[i][segment_length] != -1:
                return dp[i][segment_length]

            skip = recursive(i + 1, segment_length) % self.MOD

            take = 0
            for j in range(i + 1, n):
                take += recursive(j, segment_length + 1) % self.MOD

            dp[i][segment_length] = take + skip
            return dp[i][segment_length]

        return recursive(0, 0) % self.MOD


if __name__ == "__main__":
    testCases = [
        (4, 2, 5),
        (3, 1, 3),
        (30, 7, 796297179),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().numberOfSets(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
