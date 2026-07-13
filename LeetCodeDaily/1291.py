"""
Rank Transform of an Array
"""

from collections import deque
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = list()

        queue = deque([*range(1, 9)])

        while queue:
            num = queue.popleft()

            if low <= num <= high:
                result.append(num)

            lastDigit = num % 10

            if lastDigit + 1 <= 9:
                queue.append(num * 10 + (lastDigit + 1))

        return result

    def sequentialDigits1(self, low: int, high: int) -> List[int]:
        result = list()

        queue = deque([*range(1, 9)])

        while queue:
            num = queue.popleft()

            lastDigit = num % 10

            if lastDigit == 9:
                continue

            newNum = num * 10 + (lastDigit + 1)

            if low <= newNum <= high:
                result.append(newNum)
                queue.append(newNum)
            elif newNum > high:
                return result
            elif newNum < low:
                queue.append(newNum)

        return result


if __name__ == "__main__":
    testCases = [
        (100, 300, [123, 234]),
        (1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().sequentialDigits(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
