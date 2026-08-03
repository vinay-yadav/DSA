"""
Stone Game III
"""


class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)

        dp = [float("-inf")] * n

        def func(i):
            if i > n - 1:
                return 0

            if dp[i] != float("-inf"):
                return dp[i]

            stone2 = stone3 = float("-inf")

            stone1 = stoneValue[i] - func(i + 1)

            if i + 1 <= n - 1:
                stone2 = (stoneValue[i] + stoneValue[i + 1]) - func(i + 2)

            if i + 2 <= n - 1:
                stone3 = (stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2]) - func(
                    i + 3
                )

            dp[i] = max(stone1, stone2, stone3)
            return dp[i]

        alice_sum = func(0)

        if alice_sum == 0:
            return "Tie"
        elif alice_sum > 0:
            return "Alice"
        return "Bob"

    def stoneGameIII1(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [float("-inf")] * n
        total = sum(stoneValue)

        def func(i):
            if i > n - 1:
                return 0

            if dp[i] != float("-inf"):
                return dp[i]

            stone2 = stone3 = float("-inf")

            stone1 = stoneValue[i] + min(func(i + 2), func(i + 3), func(i + 4))

            if i + 1 <= n - 1:
                stone2 = (
                    stoneValue[i]
                    + stoneValue[i + 1]
                    + min(func(i + 3), func(i + 4), func(i + 5))
                )

            if i + 2 <= n - 1:
                stone3 = (
                    stoneValue[i]
                    + stoneValue[i + 1]
                    + stoneValue[i + 2]
                    + min(func(i + 4), func(i + 5), func(i + 6))
                )

            dp[i] = max(stone1, stone2, stone3)
            return dp[i]

        alice_sum = func(0)
        bob_sum = total - alice_sum

        if alice_sum == bob_sum:
            return "Tie"
        elif alice_sum > bob_sum:
            return "Alice"
        return "Bob"


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3, 7], "Bob"),
        ([1, 2, 3, -9], "Alice"),
        ([1, 2, 3, 6], "Tie"),
        ([-1, -2, -3], "Tie"),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().stoneGameIII1(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
