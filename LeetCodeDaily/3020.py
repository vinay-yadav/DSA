"""
Find the Maximum Number of Elements in Subset
"""

from collections import defaultdict
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1

        if mp[1] % 2:
            result = mp[1]
        else:
            result = mp[1] - 1

        for num in mp:
            if num == 1:
                continue

            curr = num
            length = 0

            while curr in mp and mp[curr] > 1:
                length += 2
                curr = curr * curr

            if curr in mp:
                length += 1
            else:
                length -= 1

            result = max(result, length)

        return result


if __name__ == "__main__":
    testCases = [([5, 4, 1, 2, 2], 3), ([1, 3, 2, 4], 1)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maximumLength(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
