"""
Shortrest and Lexicographically Smallest Beautiful String
"""


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        beautifulString = ""

        i = j = onesCount = 0
        while j < n:
            if s[j] == "1":
                onesCount += 1

            while onesCount > k or (i < j and s[i] == "0"):
                if s[i] == "1":
                    onesCount -= 1
                i += 1

            if onesCount == k:
                temp = s[i : j + 1]
                tempLen = j - i + 1

                if (
                    beautifulString == ""
                    or len(beautifulString) > tempLen
                    or (tempLen == len(beautifulString) and temp < beautifulString)
                ):
                    beautifulString = temp

            j += 1

        return beautifulString


if __name__ == "__main__":
    testCases = [
        ("100011001", 3, "11001"),
        ("1011", 2, "11"),
        ("000", 1, ""),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().shortestBeautifulSubstring(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
