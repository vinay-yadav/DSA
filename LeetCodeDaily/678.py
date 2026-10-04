"""
Valid Parenthesis String
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        dp = [[None for _ in range(n + 1)] for _ in range(n + 1)]

        def solve(idx, balance) -> bool:
            if idx == n:
                return balance == 0

            if balance < 0:
                return False

            if dp[idx][balance] is not None:
                return dp[idx][balance]

            char = s[idx]

            if char == "(":
                ans = solve(idx + 1, balance + 1)
            elif char == ")":
                ans = solve(idx + 1, balance - 1)
            else:
                ans = (
                    solve(idx + 1, balance)
                    or solve(idx + 1, balance + 1)
                    or solve(idx + 1, balance - 1)
                )

            dp[idx][balance] = ans
            return ans

        return solve(0, 0)


if __name__ == "__main__":
    testCases = [
        ("()", True),
        ("(*)", True),
        ("(*))", True),
        ("(", False),
        (")*(", False),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().checkValidString(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
