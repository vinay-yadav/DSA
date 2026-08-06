"""
Smallest Divisible Digit Product I
"""


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n, 101):
            if self.get_digits_product(num) % t == 0:
                return num

        return -1

    def get_digits_product(self, num) -> int:
        product = 1
        while num > 0:
            num, digit = divmod(num, 10)
            product *= digit
        return product


if __name__ == "__main__":
    testCases = [
        (10, 2, 10),
        (15, 3, 16),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().smallestNumber(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
