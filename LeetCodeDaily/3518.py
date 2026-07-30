"""
Smallest Palindromic Rearrangement II
"""


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half_len = n // 2  # only need to decide the first half; second half mirrors it

        result = list(s)
        base = ord("a")
        freq = [0] * 26  # frequency of each letter in the first half

        # slots_left tracks how many half-positions are still unfilled
        slots_left = 0
        for i in range(half_len):
            idx = ord(s[i]) - base
            freq[idx] += 1
            slots_left += 1

        # Greedily fix each position i, trying letters a -> z (smallest first)
        for i in range(half_len):
            placed = False

            for letter in range(26):
                if freq[letter] < 1:
                    continue

                # Tentatively place `letter` at position i
                freq[letter] -= 1
                slots_left -= 1

                # scratch counter: shrinks as we account for each remaining
                # letter type while counting arrangements of the rest of the half
                scratch_slots = slots_left

                # Count how many distinct arrangements are possible for the
                # remaining positions, given the remaining letter frequencies
                # (capped at k by nCr, since we only care whether it's >= k)
                arrangements = 1
                for c in range(26):
                    if freq[c] < 1:
                        continue

                    arrangements *= self.nCr(scratch_slots, freq[c], k)
                    scratch_slots -= freq[c]

                    if arrangements >= k:
                        break

                if arrangements >= k:
                    # Enough arrangements exist with `letter` fixed here ->
                    # commit to it and move to the next position
                    result[i] = chr(letter + base)
                    placed = True
                    break

                # Not enough arrangements with `letter` here -> skip past
                # all of them, undo the tentative placement, try next letter
                k -= arrangements
                freq[letter] += 1
                slots_left += 1

            if not placed:
                # k exceeded the total number of distinct palindromic
                # permutations available
                return ""

        # Mirror the first half onto the second half
        for i in range(half_len):
            result[n - i - 1] = result[i]

        return "".join(result)

    def nCr(self, n: int, r: int, k: int) -> int:
        """
        Computes C(n, r), capped at k (returns k if the true value would
        exceed k), to avoid computing enormous factorials unnecessarily.
        """

        # nCr == nC(n-r)
        # 5C3 == 5C2
        # 5C2 == 5C(5-2) = 5C3
        r = min(r, n - r)

        result = 1
        for i in range(1, r + 1):
            result = result * (n - r + i) // i

            if result >= k:
                return k

        return result


if __name__ == "__main__":
    testCases = [
        ("aa", 2, ""),
        ("abba", 2, "baab"),
        ("bacab", 1, "abcba"),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().smallestPalindrome(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
