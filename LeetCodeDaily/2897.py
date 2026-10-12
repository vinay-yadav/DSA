"""
Apply Operations on Array to Maximize Sum of Squares
"""


class Solution:
    MOD = 1_000_000_007

    def maxSum(self, nums: list[int], k: int) -> int:
        count = [0] * 32
        for num in nums:
            for b in range(32):
                if num & (1 << b):
                    count[b] += 1

        result = 0
        for _ in range(k):
            num = 0
            for b in range(32):
                if count[b] == 0:
                    continue

                count[b] -= 1
                num |= 1 << b

            result = (result + num * num) % self.MOD

        return result


if __name__ == "__main__":
    testCases = [
        ([2, 6, 5, 8], 2, 261),
        ([4, 5, 4, 7], 3, 90),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxSum(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
