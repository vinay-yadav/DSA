"""
Number of Unique XOR Triplets I
"""


class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        """
        T.C: O(1)
        """
        n = len(nums)

        if n <= 2:
            return n

        return 1 << n.bit_length()

    def uniqueXorTriplets1(self, nums: list[int]) -> int:
        """
        T.C: O(logn)
        """
        n = len(nums)

        if n <= 2:
            return n

        ans = 1
        while ans <= n:
            ans *= 2

        return ans


if __name__ == "__main__":
    testCases = [
        ([1, 2], 2),
        ([3, 1, 2], 4),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().uniqueXorTriplets(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
