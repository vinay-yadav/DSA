"""
Number of ZigZag Arrays II
"""

import numpy as np


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1_000_000_007
        m = r - l + 1

        vec = np.array([1] * (2 * m), dtype=object)

        T = [[0] * (2 * m) for _ in range(2 * m)]
        for x in range(m):
            for y in range(x + 1, m):
                T[x][m + y] = 1  # "must increase" -> "must decrease"
        for x in range(m):
            for y in range(x):
                T[m + x][y] = 1  # "must decrease" -> "must increase"
        T = np.array(T, dtype=object)

        def mat_pow_vec(mat, vec, power):
            result = vec
            while power:
                if power & 1:
                    result = (mat @ result) % MOD
                mat = (mat @ mat) % MOD
                power >>= 1
            return result

        final = mat_pow_vec(T, vec, n - 1)
        return int(sum(final) % MOD)


if __name__ == "__main__":
    testCases = [
        (3, 4, 5, 2),
        (3, 1, 3, 10),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().zigZagArrays(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
