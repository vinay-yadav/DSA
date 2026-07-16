"""
Sum of GCD of Formed Pairs
"""

import math


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        """
        Without mx array
        """
        n = len(nums)
        result = 0

        curr = nums[0]
        prefixGcd = [0] * n
        prefixGcd[0] = nums[0]

        for i in range(1, n):               # O(n)
            curr = max(nums[i], curr)
            prefixGcd[i] = math.gcd(curr, nums[i])

        prefixGcd.sort()                    # O(nlogn)

        i, j = 0, n - 1
        while i < j:                        # O(n)
            result += math.gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return result

    def gcdSum1(self, nums: list[int]) -> int:
        """
        With mx array
        """
        n = len(nums)
        result = 0

        mx = [0] * n
        mx[0] = nums[0]

        prefixGcd = [0] * n
        prefixGcd[0] = math.gcd(nums[0], mx[0])

        for i in range(1, n):               # O(n)
            mx[i] = max(nums[i], mx[i - 1])
            prefixGcd[i] = math.gcd(mx[i], nums[i])

        prefixGcd.sort()                    # O(nlogn)

        i, j = 0, n - 1
        while i < j:                        # O(n)
            result += math.gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return result


if __name__ == "__main__":
    testCases = [
        ([2, 6, 4], 2),
        ([3, 6, 2, 8], 5),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().gcdSum(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
