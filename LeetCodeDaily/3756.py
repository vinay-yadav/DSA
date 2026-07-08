"""
Concatenate Non-Zero Digits and Multiply by Sum II
"""

from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 1000000007

        n = len(s)
        result = [0] * len(queries)

        prefixSum, numUpto, nonZeroDgit, pow10 = [0] * n, [0] * n, [0] * n, [0] * n
        prefixSum[0] = numUpto[0] = int(s[0])
        nonZeroDgit[0] = 1 if s[0] != "0" else 0

        pow10[0] = 1
        for i in range(1, n):
            if s[i] == "0":
                numUpto[i] = numUpto[i - 1]
            else:
                numUpto[i] = ((numUpto[i - 1] * 10) + int(s[i])) % MOD

            nonZeroDgit[i] = nonZeroDgit[i - 1] + (1 if s[i] != "0" else 0)
            prefixSum[i] = prefixSum[i - 1] + int(s[i])
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for idx, q in enumerate(queries):
            start, end = q

            if start == 0:
                total = prefixSum[end]
                x = numUpto[end]
            else:
                total = prefixSum[end] - prefixSum[start - 1]
                k = nonZeroDgit[end] - nonZeroDgit[start - 1]
                lo, hi = numUpto[start - 1], numUpto[end]
                x = (hi - (lo * pow10[k] % MOD) + MOD) % MOD

            result[idx] = (total * x) % MOD

        return result


if __name__ == "__main__":
    testCases = [
        ("10203004", [[0, 7], [1, 3], [4, 6]], [12340, 4, 9]),
        ("1000", [[0, 3], [1, 1]], [1, 0]),
        ("9876543210", [[0, 9]], [444444137]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().sumAndMultiply(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
