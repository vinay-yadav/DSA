"""
Sorted GCD Pair Queries
"""

import math


class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_val = max(nums)

        # freq[x] = how many times x appears in nums
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1

        # cnt[g] = how many elements are divisible by g
        cnt = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            for multiple in range(g, max_val + 1, g):
                cnt[g] += freq[multiple]

        # exact[g] = number of pairs with gcd exactly g
        exact = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            total = cnt[g] * (cnt[g] - 1) // 2  # C(cnt[g], 2)
            for multiple in range(2 * g, max_val + 1, g):
                total -= exact[multiple]
            exact[g] = total

        # build prefix sums of pair-counts, in ascending order of g
        prefix = []
        running = 0
        gcd_values_sorted = []  # the g's that actually have exact[g] > 0
        for g in range(1, max_val + 1):
            if exact[g] > 0:
                running += exact[g]
                prefix.append(running)
                gcd_values_sorted.append(g)

        # manual binary search: first index where prefix[idx] > q
        def find_index(q):
            lo, hi = 0, len(prefix) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] > q:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        # answer each query
        answer = []
        for q in queries:
            idx = find_index(q)
            answer.append(gcd_values_sorted[idx])

        return answer

    def gcdValues1(self, nums: list[int], queries: list[int]) -> list[int]:
        result = list()
        temp = list()

        self.subSequencePair(0, nums, result, temp)
        result.sort()
        return [result[q] for q in queries]

    def subSequencePair(self, position, nums, resultList, tempList):
        if len(tempList) == 2:
            resultList.append(math.gcd(tempList[0], tempList[1]))
            return

        for i in range(position, len(nums)):
            tempList.append(nums[i])
            self.subSequencePair(i + 1, nums, resultList, tempList)
            tempList.pop()


if __name__ == "__main__":
    testCases = [
        ([2, 3, 4], [0, 2, 2], [1, 2, 2]),
        ([4, 4, 2, 1], [5, 3, 1, 0], [4, 2, 1, 1]),
        ([2, 2], [0, 0], [2, 2]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().gcdValues(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
