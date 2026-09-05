"""
Smallest Stable Index II
"""


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        rightRangeMin = [-1] * n
        rightRangeMin[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            rightRangeMin[i] = min(rightRangeMin[i + 1], nums[i])

        leftMax = float("-inf")
        instabilityScore = float("inf")
        for i in range(n):
            leftMax = max(leftMax, nums[i])
            if leftMax - rightRangeMin[i] <= k:
                instabilityScore = min(instabilityScore, i)

        return instabilityScore if instabilityScore != float("inf") else -1  # type: ignore


if __name__ == "__main__":
    testCases = [
        ([5, 0, 1, 4], 3, 3),
        ([3, 2, 1], 1, -1),
        ([0], 0, 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().firstStableIndex(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
