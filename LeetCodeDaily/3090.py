"""
Maximum Length Substring With Two Occurrences
"""

from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        freq = defaultdict(int)
        max_length_substring = 0

        i = j = 0
        while j < n:
            freq[s[j]] += 1

            while i <= j and freq[s[j]] > 2:
                freq[s[i]] -= 1
                i += 1

            max_length_substring = max(max_length_substring, j - i + 1)
            j += 1

        return max_length_substring


if __name__ == "__main__":
    testCases = [
        ("bcbbbcba", 4),
        ("aaaa", 2),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maximumLengthSubstring(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
