"""
Smallest Palindromic Rearrangement II
"""


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half_point = n // 2

        t = list(s)
        base = ord("a")
        count = [0] * 26

        for i in range(half_point):
            ch = s[i]
            idx = ord(ch) - base
            count[idx] += 1

        for i in range(half_point):
            characterPlaced = False
            for j in range(26):
                if count[j] < 1:
                    continue

                count[j] -= 1

                letters = 0
                for c in range(26):
                    letters += count[c]

                ways = 1
                for c in range(26):
                    if count[c] < 1:
                        continue

                    ways *= self.nCr(letters, count[c], k)
                    letters -= count[c]

                    if ways >= k:
                        break

                if ways >= k:
                    t[i] = chr(j + base)
                    characterPlaced = True
                    break

                k -= ways
                count[j] += 1

            if not characterPlaced:
                return ""

        for i in range(half_point):
            t[n - i - 1] = t[i]

        return "".join(t)

    def nCr(self, n, r, k):
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
