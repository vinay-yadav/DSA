"""
Palindrome Number
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        T.C: O(logx)
        S.C: O(1)
        """
        if x < 0:
            return False

        temp = x
        reverseNum = 0

        while temp > 0:
            temp, digit = divmod(temp, 10)
            reverseNum = reverseNum * 10 + digit

        return reverseNum == x

    def isPalindrome1(self, x: int) -> bool:
        """
        T.C: O(logx)
        S.C: O(d)
        """
        if x < 0:
            return False

        temp = x
        powTemp = 1
        pow10 = []
        totalDigits = 0
        while temp > 0:
            temp, _ = divmod(temp, 10)
            totalDigits += 1
            pow10.append(powTemp)
            powTemp *= 10

        temp = x
        reverseNum = 0
        while temp > 0:
            temp, digit = divmod(temp, 10)
            reverseNum += digit * pow10[totalDigits - 1]
            totalDigits -= 1

        return reverseNum == x


if __name__ == "__main__":
    testCases = [
        (10, False),
        (123, False),
        (4994, True),
        (121, True),
        (1001, True),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().isPalindrome(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
