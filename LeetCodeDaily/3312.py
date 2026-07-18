"""
Sorted GCD Pair Queries
"""

import math


class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        maxValue = max(nums)

        divisorFreq = [0] * (maxValue + 1)
        for num in nums:
            j = 1
            while j * j <= num:
                if num % j == 0:
                    divisorFreq[j] += 1

                    if (num // j) != j:
                        divisorFreq[num // j] += 1

                j += 1

        pairsWithGcd = [0] * (maxValue + 1)
        for g in range(maxValue, 0, -1):
            count = divisorFreq[g]
            if count < 2:
                continue

            # nc2
            pairsWithGcd[g] = (count * (count - 1)) // 2

            # correction
            for mult in range(2 * g, maxValue + 1, g):
                pairsWithGcd[g] -= pairsWithGcd[mult]

        prefixCountGcd = [0] * (maxValue + 1)
        for i in range(1, maxValue + 1):
            prefixCountGcd[i] = prefixCountGcd[i - 1] + pairsWithGcd[i]

        result = list()

        for idx in queries:
            left, right = 1, maxValue

            temp = 1

            while left <= right:
                mid = left + (right - left) // 2

                if prefixCountGcd[mid] > idx:
                    temp = mid
                    right = mid - 1
                else:
                    left = mid + 1

            result.append(temp)

        return result

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
        ([5, 10, 4], [0, 1, 2], [1, 2, 5]),
        ([2, 3, 4], [0, 2, 2], [1, 2, 2]),
        ([4, 4, 2, 1], [5, 3, 1, 0], [4, 2, 1, 1]),
        ([2, 2], [0, 0], [2, 2]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().gcdValues(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
