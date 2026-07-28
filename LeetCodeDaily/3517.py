"""
Smallest Palindromic Rearrangement I
"""


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        base = ord("a")
        half_len = n // 2  # number of chars in the first half
        result = list(s)

        # Step 1: count character frequencies in the first half
        # TC: O(n)
        char_count = [0] * 26
        for i in range(half_len):
            char_count[ord(s[i]) - base] += 1

        # Step 2: place characters in ascending order into the first half
        # TC: O(26 + n) ~ O(n)
        pos = 0
        for char_idx in range(26):
            ch = chr(char_idx + base)
            count = char_count[char_idx]
            while count > 0:
                result[pos] = ch
                pos += 1
                count -= 1

        # Step 3: mirror the first half onto the second half
        # (middle character, if any, is left untouched — already correct)
        # TC: O(n)
        for i in range(half_len):
            result[n - 1 - i] = result[i]

        return "".join(result)

    def naive(self, s: str) -> str:
        total_character = 26
        char_freq = [0] * total_character
        base = ord("a")
        n = len(s)

        result = [""] * n

        for ch in s:
            idx = ord(ch) - base
            char_freq[idx] += 1

        i, j = 0, n - 1

        for idx in range(total_character):
            ch = chr(idx + base)

            temp = char_freq[idx]

            if temp & 1 == 1:
                mid = (i + j) // 2
                result[mid] = ch
                temp -= 1

            while temp > 0:
                result[i] = ch
                result[j] = ch

                i += 1
                j -= 1
                temp -= 2

        return "".join(result)


if __name__ == "__main__":
    testCases = [
        ("z", "z"),
        ("babab", "abbba"),
        ("daccad", "acddca"),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().smallestPalindrome(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
