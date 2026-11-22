"""
Check if All A's Appears Before All B's
"""


class Solution:
    def checkString(self, s: str) -> bool:
        last_b = -1

        for idx, char in enumerate(s):
            if char == "a":
                if last_b != -1 and last_b < idx:
                    return False

            else:
                last_b = idx

        return True


if __name__ == "__main__":
    testCases = [
        ("aaabbb", True),
        ("abab", False),
        ("bbb", True),
        ("baab", False),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().checkString(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
