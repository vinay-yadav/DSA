"""
Process String with Special Operations I
"""


class Solution:
    def processStr(self, s: str) -> str:
        result = ""

        for chr in s:
            if chr == "*":
                result = result[:-1] if result != "" else ""
            elif chr == "#":
                result += result
            elif chr == "%":
                result = result[::-1]
            else:
                result += chr

        return result


if __name__ == "__main__":
    testCases = [("a#b%*", "ba"), ("z*#", "")]

    for idx, (s, expected) in enumerate(testCases):
        result = Solution().processStr(s)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
