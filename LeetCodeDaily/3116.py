"""
Kth Smallest Amount With Single Denomination Combination
"""

import math


class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        result = -1
        left, right = 1, max(coins) * k

        while left <= right:
            mid = left + (right - left) // 2

            if self.counteSmaller(mid, coins) >= k:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

    def counteSmaller(self, mid, coins) -> int:
        correctedCoount = 0
        n = len(coins)

        for expressions in range(1, (1 << n)):
            lcm = 0
            order = 0  # even or odd order of expressions

            for i in range(n):
                if expressions & (1 << i):
                    order += 1

                    if lcm == 0:
                        lcm = coins[i]
                    else:
                        lcm = lcm * coins[i] // math.gcd(lcm, coins[i])

            if order % 2 == 0:
                correctedCoount -= mid // lcm
            else:
                correctedCoount += mid // lcm

        return correctedCoount


if __name__ == "__main__":
    testCases = [
        ([3, 6, 9], 3, 9),
        ([5, 2], 7, 12),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findKthSmallest(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
