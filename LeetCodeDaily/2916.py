"""
Subarrays Distinct Element Sum of Squares II
"""


class Solution:
    MOD = 1_000_000_007

    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)

        sqSumSegTree = [0] * 4 * n
        sumSegTree = [0] * 4 * n
        lazyTree = [0] * 4 * n

        def lazyAddition(idx, low, high, val):
            cnt = high - low + 1
            sqSumSegTree[idx] += 2 * val * sumSegTree[idx] + cnt * val * val
            sumSegTree[idx] += cnt * val

        def updateRange(start, end, idx, low, high, val):
            if lazyTree[idx] != 0:
                lazyAddition(idx, low, high, lazyTree[idx])
                if low != high:
                    lazyTree[2 * idx + 1] += lazyTree[idx]
                    lazyTree[2 * idx + 2] += lazyTree[idx]
                lazyTree[idx] = 0  # no return here

            if low > end or high < start:
                return

            if start <= low and high <= end:
                lazyAddition(idx, low, high, val)
                if low != high:
                    lazyTree[2 * idx + 1] += val
                    lazyTree[2 * idx + 2] += val
                return

            mid = (low + high) // 2
            updateRange(start, end, 2 * idx + 1, low, mid, val)
            updateRange(start, end, 2 * idx + 2, mid + 1, high, val)

            sumSegTree[idx] = sumSegTree[2 * idx + 1] + sumSegTree[2 * idx + 2]
            sqSumSegTree[idx] = sqSumSegTree[2 * idx + 1] + sqSumSegTree[2 * idx + 2]

        lastSeenIdx = [-1] * 1_000_01
        result = 0

        for i in range(n):
            num = nums[i]

            start = lastSeenIdx[num] + 1
            end = i

            updateRange(start, end, 0, 0, n - 1, 1)
            result = (result + sqSumSegTree[0]) % self.MOD

            lastSeenIdx[num] = i

        return result


if __name__ == "__main__":
    testCases = [
        ([1, 2, 1], 15),
        ([1, 1], 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().sumCounts(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
