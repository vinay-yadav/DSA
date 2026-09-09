"""
Count Commad in Range II
"""


class Solution:
    def countCommas(self, n: int) -> int:
        result = 0
        start = 1000

        while start <= n:
            result += n - start + 1
            start *= 1000

        return result

    def countCommas1(self, n: int) -> int:
        result = 0
        comma = 1
        lower = 1000

        while lower <= n:
            upper = min(lower * 1000 - 1, n)

            count = upper - lower + 1
            result += count * comma

            lower *= 1000
            comma += 1

        return result


if __name__ == "__main__":
    testCases = [
        (1002, 3),
        (998, 0),
        (458999, 458000),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countCommas(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
