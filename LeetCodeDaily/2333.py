"""
Minimum Sum of Squared Difference
"""

import heapq


class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        k = k1 + k2

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        MAX = max(diff) + 1
        count_diff = [0] * MAX

        for idx in diff:
            count_diff[idx] += 1

        for idx in range(MAX - 1, 0, -1):
            count = count_diff[idx]
            if count == 0:
                continue

            count_ops = min(count, k)
            count_diff[idx] -= count_ops
            count_diff[idx - 1] += count_ops
            k -= count_ops

            if k == 0:
                break

        result = 0
        for idx in range(MAX):
            count = count_diff[idx]
            if count == 0:
                continue

            result += count * idx * idx

        return result

    def minSumSquareDiff1(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        k = k1 + k2
        diff = [-abs(a - b) for a, b in zip(nums1, nums2)]

        heapq.heapify(diff)

        for _ in range(k):
            if diff[0] == 0:
                break

            heapq.heapreplace(diff, diff[0] + 1)

        return sum(d * d for d in diff)


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3, 4], [2, 10, 20, 19], 0, 0, 579),
        ([1, 4, 10, 12], [5, 8, 6, 9], 1, 1, 43),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minSumSquareDiff(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
