"""
Fibonacci Series

1 2 3 4 5 6 7 8  ......
0 1 1 2 3 5 8 13 ......

f(n) = f(n - 1) + f(n - 2)
"""


class Fibonacci:
    def dynamicProgramming(self, num):
        calls = 0

        if num <= 2:
            return num - 1

        dp = [-1] * (num + 1)
        dp[1], dp[2] = 0, 1

        def topDown(n):
            """
            T.C: O(n)
            S.C: O(n)
            """
            nonlocal calls, dp

            if dp[n] != -1:
                return dp[n]

            calls += 1
            print(calls)

            dp[n] = (res := topDown(n - 1) + topDown(n - 2))
            return res

        def bottomUp(n):
            """
            T.C: O(n)
            S.C: O(n) -> can be optimized to O(1)
            """
            nonlocal dp

            for i in range(3, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]

            print(dp)
            return dp[n]

        return topDown(num)
        # return bottomUp(num)

    def recursive(self, num):
        """
        T.C: O(2^n)
        S.C: O(n)
        """
        calls = 0

        def fib(n):
            nonlocal calls

            if n <= 2:
                return n - 1

            calls += 1
            print(calls)

            return fib(n - 1) + fib(n - 2)

        return fib(num)

    def basic(self, num):
        a, b = 0, 1
        result = [a, b]

        for _ in range(3, num + 1):
            a, b = b, a + b
            result.append(b)

        print(result)
        return result[-1]


if __name__ == "__main__":
    testCases = [(100, 21)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Fibonacci().dynamicProgramming(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
