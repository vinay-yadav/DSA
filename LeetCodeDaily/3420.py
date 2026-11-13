"""
Count Non-Decreasing Subarrays After K Operations
"""

from collections import deque


class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        b = nums[::-1]  # reverse so "prefix max" becomes "suffix max"
        n = len(b)
        dq = deque()  # indices, values strictly decreasing front -> back
        l = 0
        S = 0  # sum of suffix maxes over window [l..r]
        total = 0  # sum of elements in window
        ans = 0

        for r in range(n):
            total += b[r]

            # pop elements dominated by b[r]; remove their contribution to S
            while dq and b[dq[-1]] <= b[r]:
                idx = dq.pop()
                prev = dq[-1] if dq else l - 1
                S -= b[idx] * (idx - prev)

            # push r; its segment covers (prev, r]
            prev = dq[-1] if dq else l - 1
            dq.append(r)
            S += b[r] * (r - prev)

            # shrink from the left until cost <= k
            while S - total > k:
                total -= b[l]
                S -= b[dq[0]]  # front segment loses position l
                if dq[0] == l:
                    dq.popleft()
                l += 1

            ans += r - l + 1  # all subarrays [l'..r], l' >= l are valid

        return ans


if __name__ == "__main__":
    testCases = [
        ([6, 3, 1, 2, 4, 4], 7, 17),
        ([6, 3, 1, 3, 6], 4, 12),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countNonDecreasingSubarrays(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
