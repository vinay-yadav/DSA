"""
Minimum Moves to Equal Array Elements
"""


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_element = min(nums)

        moves = 0
        for num in nums:
            moves += num - min_element

        return moves


if __name__ == "__main__":
    testCases = [
        ([1, 2, 3], 3),
        ([1, 1, 1], 0),
        ([1, 2, 3, 4, 5], 10),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minMoves(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
