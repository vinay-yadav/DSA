"""
Counting Bits
"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)

        for num in range(1, n + 1):
            result[num] = result[num >> 1] + (num & 1)

        return result

    def bruteForce(self, n: int) -> list[int]:
        def countOnes(num: int) -> int:
            count = 0

            while num > 0:
                if num & 1 == 1:
                    count += 1
                num >>= 1

            return count

        return [countOnes(num) for num in range(n + 1)]


if __name__ == "__main__":
    testCases = [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countBits(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
