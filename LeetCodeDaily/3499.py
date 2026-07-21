"""
Maximize Active Section with Trade I
"""


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        activeSessions = s.count("1")
        n = len(s)

        adjacentZeroCount = []

        i = 0
        while i < n:
            if s[i] == "0":
                start = i

                while i < n and s[i] != "1":
                    i += 1

                adjacentZeroCount.append(i - start)
            else:
                i += 1

        maxActiveSession = 0

        for i in range(1, len(adjacentZeroCount)):
            maxActiveSession = max(
                maxActiveSession, adjacentZeroCount[i - 1] + adjacentZeroCount[i]
            )

        return maxActiveSession + activeSessions


if __name__ == "__main__":
    testCases = [
        ("01", 1),
        ("0100", 4),
        ("1000100", 7),
        ("01010", 4),
        ("10110", 5),
        ("010001000", 8),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxActiveSectionsAfterTrade(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
