"""
Check Divisibility by Digit Sum and Product
"""


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_product = 1
        digit_sum = 0

        temp = n
        while temp > 0:
            temp, digit = divmod(temp, 10)

            digit_sum += digit
            digit_product *= digit

        return n % (digit_sum + digit_product) == 0


if __name__ == "__main__":
    testCases = [
        (99, True),
        (23, False),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().checkDivisibility(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
