"""
Number of Substrings Containing All Three Characters
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)

        mp = {"a": 0, "b": 0, "c": 0}

        start = end = 0
        while end < n:
            mp[s[end]] += 1

            while mp["a"] > 0 and mp["b"] > 0 and mp["c"] > 0:
                result += n - end
                mp[s[start]] -= 1
                start += 1

            end += 1

        return result


if __name__ == "__main__":
    testCases = [
        ("abcabc", 10),
        ("aaacb", 3),
        ("abc", 1),
        ("ababbbc", 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().numberOfSubstrings(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
