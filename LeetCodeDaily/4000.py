"""
Largest Integer With Given Digit Sum
"""


class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        # s == 0 is a genuine edge case: the only non-negative integer whose
        # digits sum to 0 is 0 itself (not "00" or any n-digit padded form).
        # The greedy loop below would actually still produce 0 correctly even
        # without this guard, but keeping it makes the s=0 case explicit and
        # avoids relying on that being an emergent property of the recursion.
        if s == 0:
            return 0

        # Feasibility check: max possible digit sum for an n-digit number is 9*n
        # (all 9s). If s exceeds that, no valid number exists — must check this
        # BEFORE running the greedy placement, since the greedy loop below does
        # not detect infeasibility on its own (it silently clamps and drops
        # leftover sum instead of failing loudly).
        if 9 * n < s:
            return -1

        # Precompute place values (10^0, 10^1, ..., 10^(n-1)) once, so solve()
        # doesn't recompute pow(10, k) at every recursive call.
        self.pow10 = [1]
        for i in range(1, n):
            self.pow10.append(self.pow10[i - 1] * 10)

        return self.solve(0, s, n)

    def solve(self, position, totalSum, totalPosition):
        # Base case: no positions left to fill, nothing left to add.
        # (totalSum < 0 can't actually happen here given the feasibility
        # check above and the greedy clamp below, but kept as a safety net.)
        if totalSum < 0 or position == totalPosition:
            return 0

        # Greedy choice: place the largest digit (<=9) that doesn't exceed
        # the remaining sum. This is always optimal because the current
        # position's place value is strictly greater than the sum of all
        # place values after it (e.g. 100 > 90+9), so maximizing the current
        # digit first can never be beaten by any combination of later digits.
        num = min(9, totalSum)

        # Number of positions remaining AFTER this one determines the power
        # of 10 this digit occupies (leftmost digit = highest place value).
        placeValue = self.pow10[totalPosition - position - 1]

        # Place this digit, then recurse for the rest with the reduced sum.
        return num * placeValue + self.solve(
            position + 1, totalSum - num, totalPosition
        )


if __name__ == "__main__":
    testCases = [
        (2, 9, 90),
        (3, 1, 100),
        (2, 19, -1),
        (5, 0, 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().largestInteger(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
