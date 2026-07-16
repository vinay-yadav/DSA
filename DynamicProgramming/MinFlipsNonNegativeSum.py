"""
Minimum Flips to Make Array Sum Minimum Non-Negative
"""


class Solution:
    def solve(self, arr: list[int]) -> int:
        total_sum = sum(arr)
        n = len(arr)
        capacity = total_sum // 2  # target: largest subset-sum <= half of total

        self.dp: list[list[tuple[int, int]]] = [
            [(-1, -1) for _ in range(capacity + 1)] for _ in range(n + 1)
        ]

        # Base case: with 0 elements available, best sum = 0, flips = 0
        for w in range(capacity + 1):
            self.dp[0][w] = (0, 0)

        # Base case: with 0 capacity remaining, best sum = 0, flips = 0
        for i in range(n + 1):
            self.dp[i][0] = (0, 0)

        _, min_flips = self.best_sum_and_flips(n, capacity, arr)
        return min_flips

    def best_sum_and_flips(self, i: int, w: int, arr: list[int]) -> tuple[int, int]:
        """
        Returns (best_sum, min_flips): the maximum achievable sum using a
        subset of arr[0..i-1] with sum <= w, and the minimum number of
        elements needed to achieve that sum.
        """
        if self.dp[i][w] != (-1, -1):
            return self.dp[i][w]

        # Option 1: don't flip arr[i-1]
        skip_sum, skip_flips = self.best_sum_and_flips(i - 1, w, arr)

        # Option 2: flip arr[i-1], if it fits within remaining capacity
        take_sum, take_flips = 0, 0
        if arr[i - 1] <= w:
            take_sum, take_flips = self.best_sum_and_flips(i - 1, w - arr[i - 1], arr)
            take_sum += arr[i - 1]
            take_flips += 1

        # Prefer the larger sum; break ties by fewer flips
        if take_sum > skip_sum:
            best_sum, best_flips = take_sum, take_flips
        elif skip_sum > take_sum:
            best_sum, best_flips = skip_sum, skip_flips
        else:
            best_sum, best_flips = skip_sum, min(skip_flips, take_flips)

        self.dp[i][w] = (best_sum, best_flips)
        return self.dp[i][w]


if __name__ == "__main__":
    testCases = [([10, 15, 6, 3, 3], 2), ([14, 10, 4], 1), ([15, 10, 6], 1)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
