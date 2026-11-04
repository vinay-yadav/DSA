"""
Minimum Operations to Make Elements Within K Subarrays Equal
"""


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        # ---- Step 1: cost of every window of size x ----
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def update(i, c, s):
            while i <= m:
                cnt[i] += c
                sm[i] += s
                i += i & -i

        def prefix(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        LOG = m.bit_length()

        def kth(t):  # smallest rank whose prefix count >= t
            pos = 0
            for p in range(LOG, -1, -1):
                nxt = pos + (1 << p)
                if nxt <= m and cnt[nxt] < t:
                    pos = nxt
                    t -= cnt[nxt]
            return pos + 1

        cost = []
        total = 0
        for i in range(n):
            update(rank[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:  # remove element leaving the window
                update(rank[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                med = vals[kth((x + 1) // 2) - 1]
                c, s = prefix(rank[med])
                cost.append(med * c - s + (total - s) - med * (x - c))

        # ---- Step 2: DP for k non-overlapping windows ----
        INF = float("inf")
        prev = [0] * (n + 1)  # j = 0 windows: cost 0
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]


if __name__ == "__main__":
    testCases = [
        ([5, -2, 1, 3, 7, 3, 6, 4, -1], 3, 2, 8),
        ([9, -2, -2, -2, 1, 5], 2, 2, 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minOperations(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
