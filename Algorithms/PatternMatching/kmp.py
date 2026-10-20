"""
KMP
"""

from collections.abc import Sequence
from typing import Any


class KMP:
    """
    Knuth-Morris-Pratt substring search.

    Idea
    ----
    Naive search restarts from scratch after every mismatch, which costs
    O(n * m). KMP never moves the text pointer backwards. After a mismatch it
    uses what it already knows about the matched part of the pattern to decide
    how much of that match can be reused.

    Key concept: border
    -------------------
    A border of a string is a proper prefix that is also a suffix.
    For "ABAB", the borders are "AB" (and the empty string).
    If we have matched j characters of the pattern and then mismatch, the
    last j characters of the text equal pattern[:j]. The longest border of
    pattern[:j] tells us the longest prefix of the pattern that is still
    aligned with the end of the text, so we resume from there.

    LPS array ("longest proper prefix which is also a suffix")
    ----------------------------------------------------------
    lps[k] = length of the longest border of pattern[:k + 1].

        pattern: A B A B D
        lps:     0 0 1 2 0

    Complexity
    ----------
    Time:  O(n + m)  (O(m) to build lps, O(n) to scan)
    Space: O(m)      (the lps array)
    """

    def search(self, text: Sequence[Any], pattern: Sequence[Any]) -> int:
        """
        Return the start index of the first occurrence of `pattern` in
        `text`, or -1 if there is none.

        Invariant: at the top of each iteration, j is the length of the
        longest prefix of `pattern` that ends exactly at text[i - 1].

        On each step:
          - match:    advance both pointers; if j == m, the pattern is found
                      and starts at i - m.
          - mismatch, j > 0:  fall back to the next-longest border,
                      j = lps[j - 1]. i does NOT move; text[i] is compared
                      again against the shorter prefix.
          - mismatch, j == 0: nothing to reuse, so advance i.

        Why O(n): i never decreases. j increases by at most 1 per increment
        of i, and every fallback strictly decreases j, so there are at most
        n fallbacks in total (at most about 2n loop iterations).
        """
        n, m = len(text), len(pattern)

        # Edge cases: the empty pattern matches at 0; a pattern longer than
        # the text can never match, so skip building lps entirely.
        if m == 0:
            return 0
        if m > n:
            return -1

        lps = self.compute_lps(pattern)

        i = j = 0  # i indexes text, j indexes pattern
        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1

                if j == m:
                    return i - m

            elif j > 0:
                # Reuse the longest border of the matched part.
                j = lps[j - 1]

            else:
                i += 1

        return -1

    def compute_lps(self, pattern: Sequence[Any]) -> list[int]:
        """
        Build the LPS array in O(m).

        This is KMP's search run on the pattern against itself:
        `length` is the length of the current border (the pattern prefix
        that ends at idx - 1), and `idx` is the position being extended.

          - pattern[idx] == pattern[length]: the border grows by one, so
            record lps[idx] = length and move on.
          - mismatch, length > 0: try the next-shorter border,
            length = lps[length - 1]. idx does NOT advance, because the same
            character must be re-checked against the shorter border.
          - mismatch, length == 0: no border ends here, so lps[idx] stays 0.

        lps[0] is always 0 (a single character has no proper border), which
        is why idx starts at 1.

        Same amortized argument as search: length rises at most once per
        idx increment and every fallback lowers it, so total work is O(m).
        """
        m = len(pattern)
        lps = [0] * m

        length = 0
        idx = 1
        while idx < m:
            if pattern[idx] == pattern[length]:
                length += 1
                lps[idx] = length
                idx += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                idx += 1

        return lps


if __name__ == "__main__":
    testCases = [
        ("geekxgeek", "geek", 0),
        ("abcdef", "xyz", -1),
        ("ABABABD", "ABABD", 2),
        ("ab", "abc", -1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = KMP().search(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
