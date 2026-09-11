"""
Finding 3-Digit Even Numbers
"""


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        freq = [0] * 10
        evenDigitCount = 0

        result = []

        for num in digits:
            freq[num] += 1

            if num & 1 == 0:
                evenDigitCount += 1

        if evenDigitCount == 0:
            return result

        def isExhausted(num):
            return freq[num] == 0

        for i in range(1, 10):
            if isExhausted(i):
                continue
            freq[i] -= 1

            for j in range(10):
                if isExhausted(j):
                    continue
                freq[j] -= 1

                for k in range(0, 10, 2):
                    if isExhausted(k):
                        continue
                    freq[k] -= 1

                    num = (i * 100) + (j * 10) + k
                    result.append(num)

                    freq[k] += 1
                freq[j] += 1
            freq[i] += 1

        return result


if __name__ == "__main__":
    testCases = [
        ([2, 1, 3, 0], [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]),
        ([2, 2, 8, 8, 2], [222, 228, 282, 288, 822, 828, 882]),
        ([3, 7, 5], []),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findEvenNumbers(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
