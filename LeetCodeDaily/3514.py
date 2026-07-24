"""
Number of Unique XOR Triplets I
"""


class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        """
        Same as below approach, but this time instead of taking set, we took
        a fixed size array, since we know the max achievable XOR value.

        T.C.: O(n^2)
        """
        max_xor = 1 << max(nums).bit_length()
        n = len(nums)

        xor_pair = [0] * max_xor
        result = [0] * max_xor

        for i in range(n):
            for j in range(i, n):
                xor_pair[nums[i] ^ nums[j]] = 1

        for i in range(max_xor):
            if xor_pair[i] == 1:
                for num in nums:
                    result[i ^ num] = 1

        return result.count(1)

    def uniqueXorTriplets1(self, nums: list[int]) -> int:
        """
        Since XOR follows commutative property, therefore we first pre-calculated the
        XOR pair and then calculated the triplet pair by taking XOR of pre-calculated
        XOR with nums.

        T.C.: O(n^2)
        """
        n = len(nums)

        xor_pair = set()
        for i in range(n):
            for j in range(i, n):
                xor_pair.add(nums[i] ^ nums[j])

        result = set()
        for p in xor_pair:
            for num in nums:
                result.add(p ^ num)

        return len(result)


if __name__ == "__main__":
    testCases = [
        ([1, 3], 2),
        ([6, 7, 8, 9], 4),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().uniqueXorTriplets(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
