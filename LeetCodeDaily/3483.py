"""
Unique 3-Digit Even Numbers
"""


class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        freq = [0] * 10
        evenDigitCount = 0

        result = 0

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

                    result += 1

                    freq[k] += 1
                freq[j] += 1
            freq[i] += 1

        return result


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3, 4], 12),
        ([0, 2, 2], 2),
        ([6, 6, 6], 1),
        ([1, 3, 5], 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().totalNumbers(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
