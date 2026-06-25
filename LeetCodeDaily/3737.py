"""
Count Subarrays With Majority Element I
"""

from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        idx = -1
        for i in range(len(nums)):
            if nums[i] == target:
                idx = i

        if idx == -1:
            return 0
        
        n = len(nums)

        preifxSum = [0] * n
        preifxSum[0] = 1 if nums[0] == target else 0
        for i in range(1, n):
            num = 1 if nums[i] == target else 0
            preifxSum[i] = preifxSum[i - 1] + num
        
        ans = 0
        for i in range(n):
            for j in range(i, n):
                length = j - i + 1
                if i == 0:
                    count = preifxSum[j]
                else:
                    count = preifxSum[j] - preifxSum[i - 1]

                if 2 * count > length:
                    ans += 1

        return ans


if __name__ == "__main__":
    testCases = [([1, 2, 2, 3], 2, 5), ([1, 1, 1, 1], 1, 10), ([1, 2, 3], 4, 0)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countMajoritySubarrays(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
