"""
Count Subarrays With Majority Element II
"""

from collections import defaultdict
from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0

        mp = defaultdict(int)
        cumSum = validaSubArray = 0

        mp[0] = 1

        for num in nums:
            if num == target:
                validaSubArray += mp.get(cumSum, 0)
                cumSum += 1
            else:
                cumSum -= 1
                validaSubArray -= mp.get(cumSum, 0)

            mp[cumSum] += 1
            ans += validaSubArray

        return ans


if __name__ == "__main__":
    testCases = [([1, 2, 2, 3], 2, 5), ([1, 1, 1, 1], 1, 10), ([1, 2, 3], 4, 0)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countMajoritySubarrays(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
