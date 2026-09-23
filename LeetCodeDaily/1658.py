"""
Minimum Operations to Reduce X to Zero
"""


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        """
        TC: O(n)
        SC: O(1)
        Approach: Sliding Window
        """
        n = len(nums)
        numsSum = sum(nums)
        sumMinusX = numsSum - x

        longestSubArrayLength = -1

        curr = i = j = 0
        while j < n:
            curr += nums[j]

            while i <= j and curr > sumMinusX:
                curr -= nums[i]
                i += 1

            if curr == sumMinusX and j - i + 1 > longestSubArrayLength:
                longestSubArrayLength = j - i + 1
            j += 1

        if longestSubArrayLength == -1:
            return -1

        return n - longestSubArrayLength

    def minOperations1(self, nums: list[int], x: int) -> int:
        """
        TC: O(n)
        SC: O(n)
        Approach: Prefix Sum
        """
        n = len(nums)
        mp = {0: -1}
        INF_MIN = float("-inf")

        totalSum = 0
        for idx, num in enumerate(nums):
            totalSum += num
            mp[totalSum] = idx

        if totalSum < x:
            return -1

        remainingSum = totalSum - x
        longestSubArray = INF_MIN

        currSum = 0
        for i in range(n):
            currSum += nums[i]
            findSum = currSum - remainingSum

            if mp.get(findSum, 0) != 0:
                idx = mp[findSum]
                longestSubArray = max(longestSubArray, i - idx)

        return -1 if longestSubArray == INF_MIN else int(n - longestSubArray)

    def naive(self, nums: list[int], x: int) -> int:
        """
        TC: O(n^2)
        SC: O(n^2)
        Approach: DP
        """
        n = len(nums)
        INF = float("inf")

        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        def solve(i, j, k) -> int | float:
            if k == 0:
                return 0

            if k < 0 or i > j:
                return INF

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = 1 + min(
                solve(i + 1, j, k - nums[i]),  # left
                solve(i, j - 1, k - nums[j]),  # right
            )

            return dp[i][j]

        result = solve(0, n - 1, x)
        return -1 if result == INF else int(result)


if __name__ == "__main__":
    testCases = [
        ([1, 1, 4, 2, 3], 5, 2),
        ([5, 6, 7, 8, 9], 4, -1),
        ([3, 2, 20, 1, 1, 3], 10, 5),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minOperations(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
