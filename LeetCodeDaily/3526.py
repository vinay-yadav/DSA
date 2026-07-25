"""
Maximum Product of Two Digits
"""


class Solution:
    def maxProduct(self, n: int) -> int:
        """
        TC: O(logn)
        SC: O(1)
        """
        largest = second_largest = 0

        while n > 0:
            n, digit = divmod(n, 10)

            if digit > largest:
                largest, second_largest = digit, largest

            elif digit > second_largest:
                second_largest = digit

        return largest * second_largest

    def optimal(self, n: int) -> int:
        """
        TC: O(logn)
        SC: O(1)
        """
        first = second = 0

        while n > 0:
            num = n % 10

            if num > first:
                second = first
                first = num

            elif second < num <= first:
                second = num

            n //= 10
        return first * second

    def bruteForce(self, n: int) -> int:
        """
        TC: O((logn ^2)
        SC: O(logn)
        """
        tempList = []
        while n > 0:
            num = n % 10
            tempList.append(num)
            n //= 10

        tempList.reverse()

        n = len(tempList)
        result = float("-inf")
        for i in range(n):
            for j in range(i + 1, n):
                result = max(result, tempList[i] * tempList[j])

        return result


if __name__ == "__main__":
    testCases = [
        (31, 3),
        (22, 4),
        (124, 8),
        (437, 28),
        (123456789, 72),
        (192837465, 72),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxProduct(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
