"""
Concatenate Non-Zero Digits and Multiply by Sum I
"""


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0

        num = list()
        sm = 0

        while n > 0:
            dig = n % 10

            if dig != 0:
                num.append(str(dig))
                sm += dig

            n //= 10
        num.reverse()
        return int("".join(num)) * sm


if __name__ == "__main__":
    testCases = [(10203004, 12340), (1000, 1), (0, 0)]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().sumAndMultiply(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
