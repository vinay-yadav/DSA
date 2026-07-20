"""
Fibonacci Number
"""


class Solution:
    def fib(self, n: int) -> int:
        self.calls = 0
        self.dp = [-1] * (n + 1)
        self.dp[0] = 0
        self.dp[1] = 1
        t = self.func(n)
        print(self.calls)
        return t

    def func(self, i):
        if self.dp[i] != -1:
            return self.dp[i]
        
        self.calls += 1
        self.dp[i] = self.func(i - 1) + self.func(i - 2)
        return self.dp[i]


if __name__ == "__main__":
    testCases = [(2, 1), (3, 2), (4, 3)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().fib(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
