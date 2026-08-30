"""
Sum of Decoded Numbers
"""


class Solution:
    MOD = 1_000_000_007

    def sumDecoded(self, nums: list[int]) -> int:
        total = 0
        for num in nums:
            width = num % 10
            d = num // 10

            base, exponent = self._split_payload(d, width)
            total = (total + pow(base, exponent, self.MOD)) % self.MOD

        return total

    def _split_payload(self, payload: int, width: int) -> tuple[int, int]:
        """
        Splits `payload` into (x, y) where x is formed by the first `width`
        digits and y is formed by the remaining trailing digits.
        """
        digits_least_significant_first = []
        while payload > 0:
            payload, digit = divmod(payload, 10)
            digits_least_significant_first.append(digit)

        split_index = len(digits_least_significant_first) - width
        y_digits = digits_least_significant_first[
            :split_index
        ]  # trailing digits of payload
        x_digits = digits_least_significant_first[
            split_index:
        ]  # leading digits of payload

        x = self._digits_to_number(x_digits)
        y = self._digits_to_number(y_digits)
        return x, y

    @staticmethod
    def _digits_to_number(digits_least_significant_first: list[int]) -> int:
        value = 0
        for digit in reversed(digits_least_significant_first):
            value = value * 10 + digit
        return value


if __name__ == "__main__":
    testCases = [
        ([231], 8),
        ([2522, 2101], 1649),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().sumDecoded(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
