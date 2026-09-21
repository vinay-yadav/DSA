"""
Find X Value of Array I
"""

from collections import defaultdict


class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        """
        TC: O(k.n)
        SC: O(k)
        """
        n = len(nums)
        result = [0] * k
        prevCount = [0] * k

        for i in range(n):
            currCount = [0] * k

            currentEleRemain = nums[i] % k
            currCount[currentEleRemain] += 1

            for oldRemain in range(k):
                newRemain = (oldRemain * nums[i] % k) % k

                currCount[newRemain] += prevCount[oldRemain]

            prevCount = currCount

            for x in range(k):
                result[x] += prevCount[x]

        return result

    def bruteForce(self, nums: list[int], k: int) -> list[int]:
        """
        TC: O(k.n^2)
        SC: O(k)
        """
        n = len(nums)
        result = defaultdict(int)

        for p in range(k):
            for i in range(n):
                curr = 1

                for j in range(i, n):
                    curr *= nums[j]

                    if curr % k == p:
                        result[p] += 1

        return [result[i] for i in range(k)]


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3, 4, 5], 3, [9, 2, 4]),
        ([1, 2, 4, 8, 16, 32], 4, [18, 1, 2, 0]),
        ([1, 1, 2, 1, 1], 2, [9, 6]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().resultArray(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
