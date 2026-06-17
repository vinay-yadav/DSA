"""
Process String with Special Operations II
"""


class Solution:
    def processStr(self, s: str, k: int) -> str:
        stringLength = 0
        n = len(s)

        for i in range(n):
            chr = s[i]
            if chr == "*":
                stringLength = stringLength - 1 if stringLength > 0 else 0
            elif chr == "#":
                stringLength *= 2
            elif chr == "%":
                continue
            else:
                stringLength += 1

        if k >= stringLength:
            return "."

        for i in range(n - 1, -1, -1):
            chr = s[i]

            if chr == "*":
                stringLength += 1
            elif chr == "#":
                stringLength //= 2
                # if k >= stringLength:
                #     k -= stringLength
                k %= stringLength
            elif chr == "%":
                k = stringLength - k - 1
            else:
                stringLength -= 1

            if stringLength == k:
                return chr

        return "."


if __name__ == "__main__":
    testCases = [("a#b%*", 1, "a"), ("cd%#*#", 3, "d"), ("z*#", 0, ".")]

    for idx, (s, k, expected) in enumerate(testCases):
        result = Solution().processStr(s, k)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
