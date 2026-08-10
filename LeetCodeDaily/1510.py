"""
Stone Game IV
"""


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
        TC: O(n√n)
        SC: O(n)
        """
        dp = [False] * (n + 1)

        for state in range(1, n + 1):
            i = 1
            while i * i <= state:
                if not dp[state - i * i]:
                    dp[state] = True
                    break
                i += 1

        return dp[n]

    def winnerSquareGame1(self, n: int) -> bool:
        """
        TC: O(n√n)
        SC: O(n)
        """
        dp = [-1] * (n + 1)
        dp[0] = False

        def solve(n) -> bool:
            if dp[n] != -1:
                return dp[n]

            i = 1
            win = False
            while i * i <= n:
                if not solve(n - i * i):
                    win = True
                    break

                i += 1

            dp[n] = win
            return dp[n]

        return solve(n)


if __name__ == "__main__":
    testCases = [
        (1, True),
        (2, False),
        (4, True),
        (100000, True),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().winnerSquareGame(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
