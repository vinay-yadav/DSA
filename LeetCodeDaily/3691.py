"""
Maximum Total Subarray Value II
"""

import heapq
import math
from typing import List, Tuple


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # ── Sparse Table for Range Max and Range Min ──────────────
        LOG = max(1, math.floor(math.log2(n)) + 1)

        sparse_max = [[0] * n for _ in range(LOG)]
        sparse_min = [[0] * n for _ in range(LOG)]

        sparse_max[0] = nums[:]
        sparse_min[0] = nums[:]

        for j in range(1, LOG):
            for i in range(n - (1 << j) + 1):
                sparse_max[j][i] = max(
                    sparse_max[j - 1][i], sparse_max[j - 1][i + (1 << (j - 1))]
                )
                sparse_min[j][i] = min(
                    sparse_min[j - 1][i], sparse_min[j - 1][i + (1 << (j - 1))]
                )

        def query(l, r):
            # O(1) range max - range min
            length = r - l + 1
            k = math.floor(math.log2(length))
            rng_max = max(sparse_max[k][l], sparse_max[k][r - (1 << k) + 1])
            rng_min = min(sparse_min[k][l], sparse_min[k][r - (1 << k) + 1])
            return rng_max - rng_min

        # ── Max-Heap seeded with v(l, n-1) for all l ──────────────
        # Python heapq is min-heap, negate values for max-heap
        heap = []
        for l in range(n):
            val = query(l, n - 1)
            heapq.heappush(heap, (-val, l, n - 1))

        # ── Pop k times, accumulate answer ─────────────────────────
        ans = 0
        for _ in range(k):
            neg_val, l, r = heapq.heappop(heap)
            ans += -neg_val
            # Push next candidate: shrink r by 1 (still same l)
            if r > l:
                next_val = query(l, r - 1)
                heapq.heappush(heap, (-next_val, l, r - 1))

        return ans


if __name__ == "__main__":
    testCases: List[Tuple[List[int], int, int]] = [
        ([1, 3, 2], 2, 4),
        ([4, 2, 5, 1], 3, 12),
    ]

    for idx, (nums, pivot, expected) in enumerate(testCases):
        result = Solution().maxTotalValue(nums, pivot)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
