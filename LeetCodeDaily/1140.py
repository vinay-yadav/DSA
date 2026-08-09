"""
Stone Game II
"""


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        """
        T.C: O(n ^ 2)
        S.C: O(n ^ 2)
        """
        ALICE = 0
        BOB = 1

        n = len(piles)

        # suffix_sum[i] = sum(piles[i:])
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        dp = [
            [[float("-inf") for _ in range(n + 1)] for _ in range(n + 1)]
            for _ in range(2)
        ]

        def solve(player, i, M):
            if i >= n:
                return 0

            # Short-circuit: if the player can take everything remaining
            # in one move, doing so is optimal -- no loop needed.
            if 2 * M >= n - i:
                return suffix_sum[i] if player == ALICE else 0

            if dp[player][i][M] != float("-inf"):
                return dp[player][i][M]

            result = float("-inf") if player == ALICE else float("inf")
            stones = 0

            for x in range(1, min(2 * M, n - i) + 1):
                stones += piles[i + x - 1]

                if player == ALICE:
                    result = max(result, stones + solve(BOB, i + x, max(M, x)))
                else:
                    result = min(result, solve(ALICE, i + x, max(M, x)))

            dp[player][i][M] = result
            return dp[player][i][M]

        return solve(ALICE, 0, 1)  # type: ignore

    def stoneGameII1(self, piles: list[int]) -> int:
        """
        T.C: O(n ^ 3)
        S.C: O(n ^ 2)
        """

        ALICE = 0
        BOB = 1

        n = len(piles)
        dp = [
            [[float("-inf") for _ in range(n + 1)] for _ in range(n + 1)]
            for _ in range(2)
        ]

        def solve(player, i, M):
            if i >= n:
                return 0

            if dp[player][i][M] != float("-inf"):
                return dp[player][i][M]

            result = float("-inf") if player == ALICE else float("inf")
            stones = 0

            for x in range(1, min(2 * M, n - i) + 1):
                stones += piles[i + x - 1]

                if player == ALICE:
                    result = max(result, stones + solve(BOB, i + x, max(M, x)))
                else:
                    result = min(result, solve(ALICE, i + x, max(M, x)))

            dp[player][i][M] = result

            return dp[player][i][M]

        return solve(ALICE, 0, 1)  # type: ignore


if __name__ == "__main__":
    testCases = [
        ([2, 7, 9, 4, 4], 10),
        ([1, 2, 3, 4, 5, 100], 104),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().stoneGameII(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
