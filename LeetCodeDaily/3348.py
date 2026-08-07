"""
Smallest Divisible Digit Product II
"""

from math import gcd


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        n = len(num)

        # --- Step 1: Feasibility check ---
        # A digit product can only ever contain the prime factors 2, 3, 5, 7
        # (since digits are 1-9). If t has any other prime factor, no digit
        # product can ever be divisible by t, so the answer is immediately "-1".
        leftover = t
        for prime in (2, 3, 5, 7):
            while leftover % prime == 0:
                leftover //= prime

        if leftover != 1:
            return "-1"

        # --- Step 2: Check if `num` itself already works ---
        # remaining_need[i] = the portion of t that is STILL unsatisfied
        # after using the product of the first i digits of num.
        # remaining_need[0] = t (nothing used yet).
        # remaining_need[n] == 1 means num's own digit product already
        # covers all of t's prime factors.
        #
        # NOTE: this prefix is only valid up to (but not including) the
        # first zero digit, since a 0 anywhere makes the whole product 0.
        # We stop the prefix scan as soon as we hit a 0.
        remaining_need = [t] * (n + 1)
        for i in range(n):
            digit = int(num[i])
            if digit == 0:
                break
            remaining_need[i + 1] = remaining_need[i] // gcd(remaining_need[i], digit)

        if remaining_need[n] == 1:
            # num is already zero-free (no break happened) and its digit
            # product is divisible by t.
            return num

        # --- Step 3: We must change some digit at or before the first zero ---
        first_zero_pos = num.find("0")
        last_index_to_try = n - 1 if first_zero_pos == -1 else first_zero_pos

        # Try increasing some digit at position i (keeping the prefix num[:i]
        # unchanged), then greedily fill the remaining (n - i - 1) slots with
        # the smallest possible zero-free digits whose product clears
        # whatever factor of t is still outstanding. Scan i from the
        # rightmost candidate position back to the front, since changing a
        # digit as far right as possible keeps the number smaller.
        for i in range(last_index_to_try, -1, -1):
            need_before_this_digit = remaining_need[i]
            free_slots = n - i - 1

            # Try every digit strictly greater than num[i], smallest first,
            # so the first success gives the smallest possible number.
            for candidate_digit in range(int(num[i]) + 1, 10):
                need_after_this_digit = need_before_this_digit // gcd(
                    need_before_this_digit, candidate_digit
                )
                suffix = self._smallest_suffix_covering(
                    need_after_this_digit, free_slots
                )

                if len(suffix) == free_slots:
                    return num[:i] + str(candidate_digit) + suffix
            # No digit works at this position; move left and try again.

        # --- Step 4: No same-length answer exists ---
        # Fall back to the smallest (n+1)-digit zero-free number whose
        # digit product is divisible by t.
        return self._smallest_suffix_covering(t, n + 1)

    def _smallest_suffix_covering(self, required_factor: int, length: int) -> str:
        """
        Build the smallest zero-free digit string of length `length` (or
        shorter, if fewer digits already suffice) whose digit product is
        divisible by `required_factor`.

        Greedy idea: use the largest digits (9 down to 2) first, since a
        single large digit "absorbs" more of the required factor than
        several small digits would, letting us use fewer digits overall
        -- which keeps the number as small as possible once digits are
        sorted ascending. Any slots left over after the factor is fully
        absorbed are padded with '1' (product-neutral).

        Returns digits in ascending order so it can be appended directly
        as a suffix. If it's impossible to fully cover required_factor,
        the returned string is shorter than `length` -- callers check the
        length to detect failure.
        """
        digits_used = []

        for digit in range(9, 1, -1):
            while required_factor % digit == 0:
                required_factor //= digit
                digits_used.append(str(digit))

        while len(digits_used) < length:
            digits_used.append("1")

        return "".join(reversed(digits_used))


if __name__ == "__main__":
    testCases = [
        ("1234", 256, "1488"),
        ("12355", 50, "12355"),
        ("11111", 26, "-1"),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().smallestNumber(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
