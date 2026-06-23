"""
Number of ZigZag Arrays I
"""


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        k = r - l + 1

        dp = [[0, 0] for _ in range(k + 1)]
        for v in range(k + 1):
            dp[v][0] = k - v
            dp[v][1] = v - 1

        for i in range(3, n + 1):
            nextDP = [[0, 0] for _ in range(k + 1)]
            runSum0 = 0
            for v in range(1, k + 1):
                nextDP[v][1] = runSum0
                runSum0 = (runSum0 + dp[v][0]) % MOD

            runSum1 = 0
            for v in range(k, 0, -1):
                nextDP[v][0] = runSum1
                runSum1 = (runSum1 + dp[v][1]) % MOD

            dp = nextDP

        total = 0
        for v in range(1, k + 1):
            total = (total + dp[v][0]) % MOD
            total = (total + dp[v][1]) % MOD

        return total % MOD



if __name__ == "__main__":
    testCases = [
        (3, 4, 5, 2),
        (3, 1, 3, 10),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().zigZagArrays(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
