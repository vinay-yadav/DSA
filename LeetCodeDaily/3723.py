"""
Maximize Sum of Squares of Digits
"""


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if 9 * num < sum:
            return ""

        temp_list = []
        s = sum
        for _ in range(num):
            digit = min(9, s)
            s -= digit
            temp_list.append(str(digit))

        return "".join(temp_list)


if __name__ == "__main__":
    testCases = [
        (2, 3, "30"),
        (2, 17, "98"),
        (1, 10, ""),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxSumOfSquares(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
