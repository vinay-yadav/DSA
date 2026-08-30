"""
Count Integers Appearing in a Single Block
"""


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq = [0] * 101
        first_index = [-1] * 101
        last_index = [-1] * 101

        for idx, num in enumerate(nums):
            if first_index[num] == -1:
                first_index[num] = idx

            last_index[num] = idx
            freq[num] += 1

        count = 0
        for num in set(nums):
            if last_index[num] - first_index[num] + 1 == freq[num]:
                count += 1

        return count


if __name__ == "__main__":
    testCases = [
        ([1, 2, 2, 1], 1),
        ([3, 3, 1, 2, 2, 1], 2),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countSpecialIntegers(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
