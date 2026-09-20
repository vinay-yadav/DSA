"""
Reverse Degree of a String
"""


class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for idx, char in enumerate(s):
            result += (idx + 1) * (123 - ord(char))

        return result

    def reverseDegree1(self, s: str) -> int:
        base = ord("a")

        result = 0
        for idx, char in enumerate(s):
            result += (idx + 1) * (26 - (ord(char) - base))

        return result


if __name__ == "__main__":
    testCases = [
        ("abc", 148),
        ("zaza", 160),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().reverseDegree(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
