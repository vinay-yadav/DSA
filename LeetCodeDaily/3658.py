"""
GCD of Odd and Even Sums
"""


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n

    def gcdOfOddEvenSums1(self, n: int) -> int:
        evenSum = n * (n + 1)
        oddSum = n * n
        return self.gcd(evenSum, oddSum)

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)


if __name__ == "__main__":
    testCases = [(4, 4), (5, 5)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().gcdOfOddEvenSums(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
